"""Refresh the bilingual profile README (EN + DE): stats tables plus self-rendered SVG cards.

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
TEXT = {
    "en": {
        "readme": "README.md", "thousands": ",", "date": "%Y-%m-%d",
        "header": "| 📦 Installer downloads | 🔄 Update checks | 🔀 Pull requests | ⭐ Stars |",
        "note": "Downloads and update checks count release assets across all repos. "
                "As of {date}, refreshed automatically every week.",
        "stats_title": "GitHub stats · {repos} own repos", "langs_title": "Most used languages",
        "labels": ["Commits (public)", "Pull requests", "Stars", "Installer downloads", "Update checks", "Followers"],
    },
    "de": {
        "readme": "README.de.md", "thousands": ".", "date": "%d.%m.%Y",
        "header": "| 📦 Installer-Downloads | 🔄 Update-Anfragen | 🔀 Pull Requests | ⭐ Sterne |",
        "note": "Downloads und Update-Anfragen zählen die Release-Assets aller Repos. "
                "Stand: {date}, wird wöchentlich automatisch aktualisiert.",
        "stats_title": "GitHub-Statistik · {repos} eigene Repos", "langs_title": "Meistgenutzte Sprachen",
        "labels": ["Commits (öffentlich)", "Pull Requests", "Sterne", "Installer-Downloads", "Update-Anfragen", "Follower"],
    },
}
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


def fmt(n, lang):
    return f"{n:,}".replace(",", TEXT[lang]["thousands"])


def render_table(t, lang):
    tx = TEXT[lang]
    today = datetime.date.today().strftime(tx["date"])
    values = " | ".join(f"**{fmt(t[k], lang)}**" for k in ("installs", "updates", "prs", "stars"))
    return (f"\n{tx['header']}\n|:---:|:---:|:---:|:---:|\n| {values} |\n\n"
            f"<sub>{tx['note'].format(date=today)}</sub>\n")


def svg(title, body, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{CARD_H}" '
        f'viewBox="0 0 {CARD_W} {CARD_H}" role="img" aria-label="{escape(label)}">{CARD_STYLE}'
        f'<rect class="bg" x="0.5" y="0.5" width="{CARD_W - 1}" height="{CARD_H - 1}" rx="10"/>'
        f'<text class="t" x="22" y="34">{escape(title)}</text>{body}</svg>\n'
    )


def stats_card(t, lang):
    keys = ["commits", "prs", "stars", "installs", "updates", "followers"]
    items = list(zip(TEXT[lang]["labels"], (t[k] for k in keys)))
    cells = []
    for i, (label, value) in enumerate(items):
        x, y = 22 + (i % 3) * 132, 78 + (i // 3) * 62
        cells.append(f'<text class="v" x="{x}" y="{y}">{fmt(value, lang)}</text>'
                     f'<text class="l" x="{x}" y="{y + 18}">{escape(label)}</text>')
    label = ", ".join(f"{lbl}: {v}" for lbl, v in items)
    return svg(TEXT[lang]["stats_title"].format(repos=t["repos"]), "".join(cells), label)


def languages_card(langs, lang):
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:TOP_LANGS]
    bar_w, x, parts = CARD_W - 44, 22.0, []
    for name, size in top:
        w = bar_w * size / total
        parts.append(f'<rect x="{x:.1f}" y="52" width="{max(w, 1):.1f}" height="10" '
                     f'fill="{LANG_COLORS.get(name, FALLBACK_COLOR)}"/>')
        x += w
    for i, (name, size) in enumerate(top):
        lx, ly = 22 + (i % 2) * 196, 92 + (i // 2) * 28
        parts.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{LANG_COLORS.get(name, FALLBACK_COLOR)}"/>'
                     f'<text class="l" x="{lx + 16}" y="{ly}">{escape(name)} '
                     f'{pct(size / total, lang)}</text>')
    label = ", ".join(f"{name} {pct(size / total, lang)}" for name, size in top)
    return svg(TEXT[lang]["langs_title"], "".join(parts), label)


def pct(share, lang):
    text = f"{share * 100:.1f}"
    return f"{text.replace('.', ',')} %" if lang == "de" else f"{text}%"


def main():
    readmes = {lang: ROOT / tx["readme"] for lang, tx in TEXT.items()}
    for lang, path in readmes.items():
        if not MARKER.search(path.read_text(encoding="utf-8")):
            sys.exit(f"STATS markers not found in {path.name}")
    totals, langs = collect()
    CARDS.mkdir(exist_ok=True)
    for lang, path in readmes.items():
        (CARDS / f"stats-{lang}.svg").write_text(stats_card(totals, lang), encoding="utf-8")
        (CARDS / f"languages-{lang}.svg").write_text(languages_card(langs, lang), encoding="utf-8")
        text = path.read_text(encoding="utf-8")
        path.write_text(MARKER.sub(lambda m: m.group(1) + render_table(totals, lang) + m.group(3), text),
                        encoding="utf-8")


if __name__ == "__main__":
    main()
