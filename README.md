<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:1f6feb,100:8957e5&text=Norman%20Sch%C3%B6nherr&fontColor=ffffff&fontSize=46&fontAlignY=38&desc=Automation%20%C2%B7%20KI-Tools%20%C2%B7%20Desktop-Apps&descAlignY=60&descSize=18" alt="Norman Schönherr" width="100%">

<a href="https://normanschoenherr.de"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1200&color=8957E5&center=true&vCenter=true&width=620&lines=Ich+baue+Tools%2C+die+nerviges+Zeug+automatisieren.;Karaoke-App+mit+KI-Notenerkennung+%F0%9F%8E%A4;Claude+Code+Skills+%26+MCP-Launcher+%F0%9F%A4%96;Motion-Design-Videos+per+Chat+%F0%9F%8E%AC" alt="Typing SVG"></a>

[![Projekte & Statistik](https://img.shields.io/badge/Projekte%20%26%20Live--Statistik-8957e5?style=flat-square&logo=githubpages&logoColor=white)](https://normannormalmann.github.io)
[![Website](https://img.shields.io/badge/normanschoenherr.de-1f6feb?style=flat-square&logo=googlechrome&logoColor=white)](https://normanschoenherr.de)
![Dresden](https://img.shields.io/badge/Dresden-8957e5?style=flat-square&logo=googlemaps&logoColor=white)
[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=flat-square&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/normanschou)

</div>

## 👋 Hi, ich bin Norman

Ich sitze in Dresden und baue Software, die Arbeit abnimmt: Desktop-Apps, KI-Workflows mit Claude und kleine Automatisierungen, die jeden Tag ein paar Minuten sparen. Fast alles hier ist zweisprachig (DE/EN) dokumentiert und für Leute gemacht, die keine Lust auf Kommandozeilen haben.

<!-- STATS:START -->
| 📦 Installer-Downloads | 🔄 Update-Anfragen | 🔀 Pull Requests | ⭐ Sterne |
|:---:|:---:|:---:|:---:|
| **119** | **122** | **48** | **7** |

<sub>Downloads und Update-Anfragen zählen die Release-Assets aller Repos. Stand: 24.11.2026, wird wöchentlich automatisch aktualisiert.</sub>
<!-- STATS:END -->

## 🚀 Projekte

### 🎤 [UltraStar – Dirty Little Helper](https://github.com/normannormalmann/ultrastar-dlh)

Desktop-App, die eine UltraStar-Karaoke-Sammlung aufbaut, pflegt und durchsuchbar macht. Fehlt ein Lied in der Datenbank, trennt eine KI die Stimme ab, legt den Text auf den Gesang und erkennt die Tonhöhen. Gebaut für Melody Mania, UltraStar Deluxe, Vocaluxe und UltraStar Play.

![Electron](https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
[![Release](https://img.shields.io/github/v/release/normannormalmann/ultrastar-dlh?style=flat-square&color=8957e5)](https://github.com/normannormalmann/ultrastar-dlh/releases)
[![Downloads](https://img.shields.io/github/downloads/normannormalmann/ultrastar-dlh/total?style=flat-square&color=1f6feb)](https://github.com/normannormalmann/ultrastar-dlh/releases)

<details>
<summary><b>📈 Downloads je Release ansehen</b></summary>

```mermaid
xychart-beta
    title "UltraStar DLH: Installer-Downloads vs. Update-Checks"
    x-axis ["v1.2.0", "v1.3.0", "v1.4.0", "v1.4.1", "v1.5.0", "v1.5.1", "v1.6.0", "v1.6.1"]
    y-axis "Downloads" 0 --> 90
    bar [18, 2, 28, 14, 12, 5, 8, 32]
    line [0, 0, 84, 8, 10, 4, 4, 12]
```

Balken: Installer (Windows + Linux). Linie: Update-Checks installierter Apps (`latest.yml`). v1.4.0 war zwei Monate lang die aktuelle Version und hat deshalb die meisten Update-Anfragen gesammelt.

</details>

### 🎬 [Claude Motionreel Generator](https://github.com/normannormalmann/Claude-Motionreel-Generator-CMG)

Ein eigenes Studio für KI-erstellte Motion-Design-Videos, eingerichtet mit einem Doppelklick. Du beschreibst das Video in normalen Worten, Claude baut die Animation, prüft die Einzelbilder und rendert ein MP4. Läuft auf Windows, macOS und Linux.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white)

### 🧰 Claude & Automation Toolbox

| Projekt | Was es macht | Stack |
|---|---|---|
| [**Claude-Multiverse**](https://github.com/normannormalmann/Claude-Multiverse) | Mehrere isolierte Claude-Desktop-Instanzen nebeneinander, z. B. Arbeit und Privat, ohne ständiges Ab- und Anmelden | PowerShell |
| [**meta-ads-mcp-secure-launcher**](https://github.com/normannormalmann/meta-ads-mcp-secure-launcher) | Gehärteter Launcher für den Meta-Ads-MCP: Zugangsdaten im Credential Manager, Token-Maskierung in Logs, Schreibschutz für Budgets | Python |
| [**hubspot-skills**](https://github.com/normannormalmann/hubspot-skills) | Claude Skills, die HubSpot-Sequenzen bauen, testen und Kontakte automatisch einschreiben, inklusive der Fehler, die HubSpot nicht erklärt | Claude Skills, n8n |
| [**timebutler_auto**](https://github.com/normannormalmann/timebutler_auto) | Stempelt automatisch in Timebutler ein, sobald der Rechner im Büro-WLAN ist, oder ganztägig per n8n | Python, Playwright, Docker |

<details>
<summary><b>🍴 Forks & Beiträge</b></summary>

- [streambert-german](https://github.com/normannormalmann/streambert-german): Electron-Streaming-App, um deutsche Streams erweitert
- [awesome-claude-skills](https://github.com/normannormalmann/awesome-claude-skills): kuratierte Liste von Claude Skills
- [winget-pkgs](https://github.com/normannormalmann/winget-pkgs): Fork für die Veröffentlichung im Windows Package Manager

</details>

## 🛠️ Womit ich arbeite

<p>
<img src="https://skillicons.dev/icons?i=ts,js,python,powershell,bash,electron,react,docker,githubactions,html,css,vscode" alt="Tech Stack">
</p>

## 📊 GitHub in Zahlen

> 📈 **Interaktive Statistik mit Verlauf, Filtern und Downloads pro Tag: [normannormalmann.github.io](https://normannormalmann.github.io#stats)**

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=normannormalmann&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=00000000&title_color=8957e5&icon_color=1f6feb&text_color=7d8590" alt="GitHub Stats">
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=normannormalmann&layout=compact&hide_border=true&bg_color=00000000&title_color=8957e5&text_color=7d8590&langs_count=8" alt="Top Languages">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=normannormalmann&bg_color=00000000&color=7d8590&line=8957e5&point=1f6feb&area=true&area_color=8957e5&hide_border=true" alt="Activity Graph" width="100%">

</div>

<details>
<summary><b>🥧 Wo der Code liegt (Bytes je Sprache)</b></summary>

```mermaid
pie showData
    title Code-Anteile in eigenen Repos
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
