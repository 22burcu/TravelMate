---
title: Burcu Özen
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Burcu Özen

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1.3

### Personal goals

+ Python lernen
+ Lernen wie man eine Website erstellt und gestaltet
+ Verstehen, wie man mit Flask eine Webanwendung entwickelt
+ Frontend und Backend miteinander verknüpfen
+ Neue Tools und Technologien kennenlernen

---

## Eidesstattliche Erklärung

**[Burcu Özen, Matrikelnr.: 77212025876]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Vollständigen Authentifizierungsflow implemeniert (Registrierung, Login und Logout) | Ich bin stolz darauf, einen funktionierenden und sicheren Register/Login-Bereich umgesetzt zu haben, weil die Authentifizierung der wichtigste Bestandteil der Webapp ist. | Es erforderte mich eine genaue Einarbeitung, um Sessions, Passwort-Hashing und das Zusammenspiel von Flask-Login, SQLAlchemy und dem User-Modell zu verstehen. |
| 2 | Implementierung des Profilsystems mit Anzeige und Bearbeitung der Benutzerdaten | Das Profilsystem gibt jedem Nutzer eine persönliche Identität auf der Plattform und schafft Vertrauen zwischen Hosts und Joinern. Ohne Profil wäre die Plattform anonym und das Matching zwischen Host und Joiner weniger vertrauenswürdig. | Formulardaten korrekt zu verarbeiten und Änderungen zuverlässig in der Datenbank zu speichern war herausfordernd. Außerdem musste ich verstehen wie current_user aus Flask-Login direkt im Template und in der Route verfügbar ist, ohne den User extra aus der Datenbank abzufragen. |
| 3 | Entwicklung des Dashboard-Systems für Hosts und Joiner | Ich bin stolz darauf, dass Benutzer übersichtliche Dashboards mit ihren eigenen Reisen bzw. Bewerbungen erhalten. | Es war herausfordernd, benutzerspezifische Daten mit SQLAlchemy abzufragen und die Reisen anhand des Datums in offene, aktive und vergangene Trips einzuteilen. Ich musste auch herausfinden wie Daten abhängig vom aktuell eingeloggten Benutzer gefiltert und an die Templates übergeben werden.|

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #01](../design-decisions/dd-01.md)
 
---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [Commit 1](https://github.com/hwrberlin/fswd/commit/d816e4), [Commit 2](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |         |                |                                 |                             |
| 02  |         |                |                                 |                             |
| ... |         |                |                                 |                             |
