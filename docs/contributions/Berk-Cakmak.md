---
title: Berk Cakmak
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Berk Cakmak

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1.7

### Personal goals

+ Projekte in Github kontrollieren und verwalten können
+ Webseiten designen können
+ Meine Teammitglieder unterstützen können in Hinsicht auf Programmierung und dessen Tools

---

## Eidesstattliche Erklärung

**[Berk Cakmak, Matrikelnr.: 77201549610]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Trip-Erstellung: Aufbau der `create_trip`-Seite, über die Hosts eine neue Reise mit allen Angaben anlegen können | Es ist ein vollständiges, eigenständiges Feature, das ich von Grund auf gebaut habe und ohne das die App nichts zum Durchsuchen hätte | Die Formulardaten korrekt zu erfassen und an die Datenbank bzw. die Business Rules anzubinden, sodass nur gültige Reisen gespeichert werden |
| 2 | Host- und Joiner-Dashboard: Logik in `dashboard.py`, die Reisen nach Status (offen, aktiv, vergangen) aufteilt und anzeigt, inkl. Einbindung des Blueprints | Das Dashboard ist die zentrale Übersicht für die Nutzer und führt mehrere Teile der App zusammen | Die Anzeige interativ zum Laufen zu bringen und dabei Fehler wie doppelte Tabellenzeilen aufzuspüren und zu beheben |
| 3 | Datenmodell fürs Reiseziel: Umstellung in `models.py` von einem einfachen Ortsfeld auf `origin_id`/`destination_id` plus Anpassung der IDs für eine saubere DB-Struktur | Die Entscheidung hat ein Strukturproblem gelöst und das Datenmodell sauberer gemacht | Neben der Modelländerung hatte ich technische Probleme mit Git/VS Code beim Committen, die ich erst lösen musste, um die Änderung überhaupt einzureichen |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #01](../design-decisions/dd-01.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Initiales Projekt-Setup & Trips-Modul: Grundstruktur der Flask-App, Anlage von `trips.py` und `application.py`, Einbindung als Blueprint in `__init__.py` | [f8556d9](https://github.com/22burcu/TravelMate/commit/f8556d9), [7cc3d8c](https://github.com/22burcu/TravelMate/commit/7cc3d8c), [c84d758](https://github.com/22burcu/TravelMate/commit/c84d758), [43ce0ff](https://github.com/22burcu/TravelMate/commit/43ce0ff) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/) |
| Datenmodell Reiseziel: Umstellung in `models.py` auf `origin_id`/`destination_id` und Anpassung der IDs für eine konsistente Datenbankstruktur | [940a701](https://github.com/22burcu/TravelMate/commit/940a701) | [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) |
| Trip-Erstellung: Aufbau der `create_trip`-Seite (`create_trip.html`), über die Hosts eine neue Reise mit allen Angaben anlegen | [10cee87](https://github.com/22burcu/TravelMate/commit/10cee87) | [Jinja2 Documentation](https://jinja.palletsprojects.com/) |
| Host-/Joiner-Dashboard: Logik in `dashboard.py` (Reisen nach Status offen/aktiv/vergangen), Einbindung des Dashboard-Blueprints in `__init__.py`, Bugfixes | [db071bd](https://github.com/22burcu/TravelMate/commit/db071bd), [1aadee0](https://github.com/22burcu/TravelMate/commit/1aadee0), [2619024](https://github.com/22burcu/TravelMate/commit/2619024), [0e69ff3](https://github.com/22burcu/TravelMate/commit/0e69ff3), [9aff084](https://github.com/22burcu/TravelMate/commit/9aff084) | [Flask Documentation](https://flask.palletsprojects.com/) |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |         |                |                                 |                             |
| 02  |         |                |                                 |                             |
| ... |         |                |                                 |                             |
