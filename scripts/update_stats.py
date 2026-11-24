"""Refresh the stats table in README.md from the public GitHub API.

Counts release asset downloads (installers vs. update checks), pull requests
and stars across all public, non-fork repositories of the profile owner.
"""
import datetime
import json
import os
import pathlib
import re
import sys
import urllib.request

USER = os.environ.get("GH_USER", "normannormalmann")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
MARKER = re.compile(r"(<!-- STATS:START -->)(.*?)(<!-- STATS:END -->)", re.S)


def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def classify(asset_name):
    if asset_name.startswith("latest") and asset_name.endswith(".yml"):
        return "updates"
    if asset_name.endswith((".exe", ".AppImage", ".dmg", ".msi", ".deb", ".zip")):
        return "installs"
    return "other"


def collect():
    totals = {"installs": 0, "updates": 0, "prs": 0, "stars": 0}
    repos = [r for r in api(f"users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
    for repo in repos:
        name = repo["name"]
        totals["stars"] += repo["stargazers_count"]
        totals["prs"] += len(api(f"repos/{USER}/{name}/pulls?state=all&per_page=100"))
        for release in api(f"repos/{USER}/{name}/releases?per_page=100"):
            for asset in release["assets"]:
                kind = classify(asset["name"])
                if kind in totals:
                    totals[kind] += asset["download_count"]
    return totals


def de(n):
    return f"{n:,}".replace(",", ".")


def render(t):
    today = datetime.date.today().strftime("%d.%m.%Y")
    return (
        "\n| 📦 Installer-Downloads | 🔄 Update-Anfragen | 🔀 Pull Requests | ⭐ Sterne |\n"
        "|:---:|:---:|:---:|:---:|\n"
        f"| **{de(t['installs'])}** | **{de(t['updates'])}** | **{de(t['prs'])}** | **{de(t['stars'])}** |\n\n"
        "<sub>Downloads und Update-Anfragen zählen die Release-Assets aller Repos. "
        f"Stand: {today}, wird wöchentlich automatisch aktualisiert.</sub>\n"
    )


def main():
    text = README.read_text(encoding="utf-8")
    if not MARKER.search(text):
        sys.exit("STATS markers not found in README.md")
    updated = MARKER.sub(lambda m: m.group(1) + render(collect()) + m.group(3), text)
    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
