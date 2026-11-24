"""Refresh the profile README: stats table plus two self-rendered SVG cards.

Counts release asset downloads (installers vs. update checks), pull requests,
stars, commits and code languages across all public, non-fork repositories.
The cards are written to ./cards so the README does not depend on third-party
card services.
"""
import datetime
import json
import os
import pathlib
import re
import sys
import urllib.request
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "normannormalmann")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CARDS = ROOT / "cards"
MARKER = re.compile(r"(<!-- STATS:START -->)(.*?)(<!-- STATS:END -->)", re.S)
TOP_LANGS = 6
CARD_W, CARD_H = 420, 180
LANG_COLORS = {
    "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "Python": "#3572A5", "PowerShell": "#012456",
    "Shell": "#89e051", "CSS": "#663399", "HTML": "#e34c26", "Batchfile": "#C1F12E",
    "Dockerfile": "#384d54", "Go": "#00ADD8", "Rust": "#dea584",
}
FALLBACK_COLOR = "#8b949e"
CARD_STYLE = """<style>
.bg{fill:#ffffff;stroke:#d0d7de}.t{font:600 15px 'Segoe UI',Ubuntu,sans-serif;fill:#8957e5}
.l{font:400 12px 'Segoe UI',Ubuntu,sans-serif;fill:#57606a}.v{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#1f2328}
@media (prefers-color-scheme:dark){.bg{fill:#0d1117;stroke:#30363d}.l{fill:#8b949e}.v{fill:#e6edf3}}
</style>"""


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
    if asset_name.endswith((".exe", ".AppImage", ".dmg", ".msi", ".deb", ".zip", ".skill")):
        return "installs"
    return "other"


def collect():
    totals = {"installs": 0, "updates": 0, "prs": 0, "stars": 0}
    langs = {}
    repos = [r for r in api(f"users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
    for repo in repos:
        name = repo["name"]
        totals["stars"] += repo["stargazers_count"]
        totals["prs"] += len(api(f"repos/{USER}/{name}/pulls?state=all&per_page=100"))
        for lang, size in api(f"repos/{USER}/{name}/languages").items():
            langs[lang] = langs.get(lang, 0) + size
        for release in api(f"repos/{USER}/{name}/releases?per_page=100"):
            for asset in release["assets"]:
                kind = classify(asset["name"])
                if kind in totals:
                    totals[kind] += asset["download_count"]
    totals["repos"] = len(repos)
    totals["followers"] = api(f"users/{USER}")["followers"]
    totals["commits"] = api(f"search/commits?q=author:{USER}&per_page=1")["total_count"]
    return totals, langs


def de(n):
    return f"{n:,}".replace(",", ".")


def render_table(t):
    today = datetime.date.today().strftime("%d.%m.%Y")
    return (
        "\n| 📦 Installer-Downloads | 🔄 Update-Anfragen | 🔀 Pull Requests | ⭐ Sterne |\n"
        "|:---:|:---:|:---:|:---:|\n"
        f"| **{de(t['installs'])}** | **{de(t['updates'])}** | **{de(t['prs'])}** | **{de(t['stars'])}** |\n\n"
        "<sub>Downloads und Update-Anfragen zählen die Release-Assets aller Repos. "
        f"Stand: {today}, wird wöchentlich automatisch aktualisiert.</sub>\n"
    )


def svg(title, body, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{CARD_H}" '
        f'viewBox="0 0 {CARD_W} {CARD_H}" role="img" aria-label="{escape(label)}">{CARD_STYLE}'
        f'<rect class="bg" x="0.5" y="0.5" width="{CARD_W - 1}" height="{CARD_H - 1}" rx="10"/>'
        f'<text class="t" x="22" y="34">{escape(title)}</text>{body}</svg>\n'
    )


def stats_card(t):
    items = [("Commits (öffentlich)", t["commits"]), ("Pull Requests", t["prs"]),
             ("Sterne", t["stars"]), ("Installer-Downloads", t["installs"]),
             ("Update-Anfragen", t["updates"]), ("Follower", t["followers"])]
    cells = []
    for i, (label, value) in enumerate(items):
        x, y = 22 + (i % 3) * 132, 78 + (i // 3) * 62
        cells.append(f'<text class="v" x="{x}" y="{y}">{de(value)}</text>'
                     f'<text class="l" x="{x}" y="{y + 18}">{escape(label)}</text>')
    label = ", ".join(f"{lbl}: {v}" for lbl, v in items)
    return svg(f"GitHub-Statistik · {t['repos']} eigene Repos", "".join(cells), label)


def languages_card(langs):
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:TOP_LANGS]
    bar_w, x, parts = CARD_W - 44, 22.0, []
    for lang, size in top:
        w = bar_w * size / total
        parts.append(f'<rect x="{x:.1f}" y="52" width="{max(w, 1):.1f}" height="10" '
                     f'fill="{LANG_COLORS.get(lang, FALLBACK_COLOR)}"/>')
        x += w
    for i, (lang, size) in enumerate(top):
        lx, ly = 22 + (i % 2) * 196, 92 + (i // 2) * 28
        parts.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{LANG_COLORS.get(lang, FALLBACK_COLOR)}"/>'
                     f'<text class="l" x="{lx + 16}" y="{ly}">{escape(lang)} '
                     f'{size / total * 100:.1f} %</text>')
    label = ", ".join(f"{lang} {size / total * 100:.1f} %" for lang, size in top)
    return svg("Meistgenutzte Sprachen", "".join(parts), label)


def main():
    text = README.read_text(encoding="utf-8")
    if not MARKER.search(text):
        sys.exit("STATS markers not found in README.md")
    totals, langs = collect()
    CARDS.mkdir(exist_ok=True)
    (CARDS / "stats.svg").write_text(stats_card(totals), encoding="utf-8")
    (CARDS / "languages.svg").write_text(languages_card(langs), encoding="utf-8")
    README.write_text(MARKER.sub(lambda m: m.group(1) + render_table(totals) + m.group(3), text), encoding="utf-8")


if __name__ == "__main__":
    main()
