---
title: Ariyan Serhat Shane Graf
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Ariyan Serhat Shane Graf

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

+ Python/Programmieren verbessern
+ Umgang mit Github kennenlernen
+ Lernen wie man eine Website von grundauf aufbaut
+ Teamfähigkeit verbessern
+ Lösungsorientiert arbeiten

---

## Eidesstattliche Erklärung

**[Ariyan Serhat Shane Graf, Matrikelnr.: 77209039240]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | [Zentrale Geschäftsregeln in einem eigenen Modul (business_rules.py) – Prüfung beim Anlegen eines Trips: maximal 3 offene Reisen gleichzeitig und keine zeitliche Überschneidung mit bestehenden Reisen. (Commits e344775, c3229d0)] | [Die Regeln liegen an einer zentralen Stelle statt verstreut im Code – dadurch nutzen mehrere Routen dieselbe Logik ohne Wiederholung. Das ist sauberer, wartbarer Code und zeigt echtes Verständnis von Architektur, nicht nur „es funktioniert".]  | [Die Logik für die zeitliche Überschneidung zweier Reisezeiträume war knifflig. Ich musste eine allgemeingültige Formel finden, die alle Überlappungsfälle abdeckt (Reise A in B, B in A, teilweise Überlappung), statt unzählige Einzelfälle abzufragen.] |
| 2 | [Vollständige Trip-Erstellung als Host – HTML-Formular, Umwandlung der Datumsfelder in echte Date-Objekte, Validierung der Eingaben und Speicherung in der Datenbank mit allen relevanten Eigenschaften. (Commits 2d59118, 441f1ad, 5e0c3b4, 9d6e341)] | [Das ist die Kernfunktion der Host-Seite und verbindet alle Schichten der App: Formular (Frontend) → Validierung (Logik) → Datenbank (Persistenz). Außerdem ist die Erstellung durch Rollenprüfung abgesichert, sodass nur Hosts Reisen anlegen können.] | [Formulardaten kommen immer als Text. Die größte Hürde war, die Datumsfelder korrekt in date-Objekte umzuwandeln (strptime), damit Vergleiche und die Überschneidungsregel überhaupt funktionieren – ein Fehler hier hätte die ganze Geschäftslogik unbrauchbar gemacht.] |
| 3 | [Headless JSON-API-Endpoint (GET /api/trips) – liefert alle Reisen als strukturiertes JSON statt als HTML-Seite. (Commit 79d7310)] | [Dieser Endpoint erfüllt eine zentrale Architektur-Anforderung des Projekts (eine „headless" Schnittstelle) und trennt sauber Daten von Darstellung – die Basis dafür, dass die Reisedaten auch von anderen Programmen oder einer späteren App genutzt werden könnten.] | [Ich musste verstehen, warum Datumswerte hier bewusst im technischen ISO-Format (JJJJ-MM-TT) bleiben, während sie für Menschen anders angezeigt werden – also die Unterscheidung zwischen Daten für Maschinen und Anzeige für Menschen sauber umsetzen.] |

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
