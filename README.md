<div align="center">

<sub>🇬🇧 English · 🇩🇪 <a href="https://github.com/normannormalmann/normannormalmann/blob/main/README.de.md">Deutsch</a></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:1f6feb,100:8957e5&text=Norman%20Sch%C3%B6nherr&fontColor=ffffff&fontSize=46&fontAlignY=38&desc=Automation%20%C2%B7%20AI%20Tools%20%C2%B7%20Desktop%20Apps&descAlignY=60&descSize=18" alt="Norman Schönherr" width="100%">

<a href="https://normanschoenherr.de"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1200&color=8957E5&center=true&vCenter=true&width=620&lines=I+build+tools+that+automate+the+boring+stuff.;Karaoke+app+with+AI+pitch+detection+%F0%9F%8E%A4;Claude+Code+skills+%26+MCP+launchers+%F0%9F%A4%96;Motion+design+videos+from+a+chat+%F0%9F%8E%AC" alt="Typing SVG"></a>

[![Projects & stats](https://img.shields.io/badge/Projects%20%26%20live%20stats-8957e5?style=flat-square&logo=githubpages&logoColor=white)](https://normannormalmann.github.io)
[![Website](https://img.shields.io/badge/normanschoenherr.de-1f6feb?style=flat-square&logo=googlechrome&logoColor=white)](https://normanschoenherr.de)
![Dresden, Germany](https://img.shields.io/badge/Dresden,%20Germany-8957e5?style=flat-square&logo=googlemaps&logoColor=white)
[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=flat-square&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/normanschou)

</div>

## 👋 Hi, I'm Norman

I'm based in Dresden, Germany, and I build software that takes work off people's plates: desktop apps, AI workflows with Claude and small automations that save a few minutes every day. Almost everything here is documented in English and German and made for people who'd rather not touch a command line.

<!-- STATS:START -->
| 📦 Installer downloads | 🔄 Update checks | 🔀 Pull requests | ⭐ Stars |
|:---:|:---:|:---:|:---:|
| **119** | **122** | **50** | **7** |

<sub>Downloads and update checks count release assets across all repos. As of 2026-11-24, refreshed automatically every week.</sub>
<!-- STATS:END -->

## 🚀 Projects

### 🎤 [UltraStar – Dirty Little Helper](https://github.com/normannormalmann/ultrastar-dlh)

A desktop app that builds, maintains and searches your UltraStar karaoke collection. If a song is missing from the database, an AI separates the vocals, aligns the lyrics to the singing and detects the pitches. Built for Melody Mania, UltraStar Deluxe, Vocaluxe and UltraStar Play.

![Electron](https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
[![Release](https://img.shields.io/github/v/release/normannormalmann/ultrastar-dlh?style=flat-square&color=8957e5)](https://github.com/normannormalmann/ultrastar-dlh/releases)
[![Downloads](https://img.shields.io/github/downloads/normannormalmann/ultrastar-dlh/total?style=flat-square&color=1f6feb)](https://github.com/normannormalmann/ultrastar-dlh/releases)

<details>
<summary><b>📈 Downloads per release</b></summary>

```mermaid
xychart-beta
    title "UltraStar DLH: installer downloads vs. update checks"
    x-axis ["v1.2.0", "v1.3.0", "v1.4.0", "v1.4.1", "v1.5.0", "v1.5.1", "v1.6.0", "v1.6.1"]
    y-axis "Downloads" 0 --> 90
    bar [18, 2, 28, 14, 12, 5, 8, 32]
    line [0, 0, 84, 8, 10, 4, 4, 12]
```

Bars: installers (Windows + Linux). Line: update checks from installed apps (`latest.yml`). v1.4.0 was the current version for two months, so it collected the most update checks.

</details>

### 🎬 [Claude Motionreel Generator](https://github.com/normannormalmann/Claude-Motionreel-Generator-CMG)

Your own studio for AI-made motion design videos, set up with a double-click. Describe the video in plain words, Claude builds the animation, checks the frames and renders an MP4. Runs on Windows, macOS and Linux.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white)

### 🧰 Claude & automation toolbox

| Project | What it does | Stack |
|---|---|---|
| [**Claude-Multiverse**](https://github.com/normannormalmann/Claude-Multiverse) | Run several isolated Claude Desktop instances side by side, e.g. work and private, without logging in and out | PowerShell |
| [**meta-ads-mcp-secure-launcher**](https://github.com/normannormalmann/meta-ads-mcp-secure-launcher) | Hardened launcher for the Meta Ads MCP: credentials in the Windows Credential Manager, token masking in logs, write guard for budgets | Python |
| [**hubspot-skills**](https://github.com/normannormalmann/hubspot-skills) | Claude skills that build and test HubSpot sequences and auto-enroll contacts, including the errors HubSpot doesn't explain | Claude Skills, n8n |
| [**timebutler_auto**](https://github.com/normannormalmann/timebutler_auto) | Clocks you in to Timebutler as soon as your PC joins the office Wi-Fi, or runs the whole day via n8n | Python, Playwright, Docker |

<details>
<summary><b>🍴 Forks & contributions</b></summary>

- [streambert-german](https://github.com/normannormalmann/streambert-german): Electron streaming app, extended with German streams
- [awesome-claude-skills](https://github.com/normannormalmann/awesome-claude-skills): curated list of Claude skills
- [winget-pkgs](https://github.com/normannormalmann/winget-pkgs): fork for publishing to the Windows Package Manager

</details>

## 🛠️ What I work with

<p>
<img src="https://skillicons.dev/icons?i=ts,js,python,powershell,bash,electron,react,docker,githubactions,html,css,vscode" alt="Tech stack">
</p>

## 📊 GitHub in numbers

> 📈 **Interactive stats with history, filters and downloads per day: [normannormalmann.github.io](https://normannormalmann.github.io#stats)** (in German)

<div align="center">

<img width="49%" src="cards/stats-en.svg" alt="GitHub stats: commits, pull requests, stars, downloads, update checks and followers">
<img width="49%" src="cards/languages-en.svg" alt="Most used programming languages">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=normannormalmann&bg_color=00000000&color=7d8590&line=8957e5&point=1f6feb&area=true&area_color=8957e5&hide_border=true" alt="Activity graph" width="100%">

</div>

<details>
<summary><b>🥧 Where the code lives (bytes per language)</b></summary>

```mermaid
pie showData
    title Code share across my own repos
    "TypeScript" : 981604
    "Python" : 656026
    "PowerShell" : 90019
    "JavaScript" : 44505
    "Shell" : 25066
    "CSS" : 24420
```

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:8957e5,100:1f6feb&section=footer" width="100%" alt="">
</div>
