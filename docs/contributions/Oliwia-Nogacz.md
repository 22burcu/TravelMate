---
title: Oliwia Nogacz
parent: Individual Contributions
nav_order: 1
---


{: .no_toc }
# Oliwia Nogacz

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

+ Verstehen, wie Plattformökonomie funktioniert (Angebot & Nachfrage auf einer App)
+ Zwei verschiedene Nutzerrollen technisch umsetzen (unterschiedliche Rechte, Views, Flows)
+ Ein Gefühl dafür entwickeln, was realistisch in einem Semester umsetzbar ist
+ Den Unterschied zwischen "es funktioniert" und "es ist gut gebaut" verstehen
+ Anforderungen in konkrete Tasks herunterbrechen

---

## Eidesstattliche Erklärung

**[Oliwia Nogacz, Matrikelnr.: 77211971549]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Trips-Suche + Filterfunktion + Detailseite (trips.py + trips.html trip_details.html); Suchleiste nach Reiseziel mit ilike(damit Groß und Kleinschreibung egal ist); filter nach Kontinent, Reiseart, Reiseziel, Budget, Datum; Dynamische Query bei der Filter nur angewendet werden wenn sie auch ausgefüllt werden; SQLAlchemy Join zwischen Trip und Location Tabelle | Backend(Python/SQLAlchemy) und Frontend(Bootstrap/Jinja2) mussten gleichzeitig zusammenspielen. Der Join zwischen Trip und Location war technisch sehr anspruchvoll und Zeitaufwendig. Ich habe mehrere Bugs selbst gefunden und gefixt, das ist mir früher nicht gelungen. Ich habe nicht aufgegeben.| Die dynamische Query war herausfordernd, Filter dürften nur angewendet werden wenn sie auch ausgefüllt sind, sonst werden alle Trips herausgefiltert. Ich musste lernen wie man eine Query Schrittweise aufbaut. Arbeit am Frontend und Backend gleichzeitig, verschiedene Codierungsansätze gleichzeitig.|
| 2 | Bewerbungssystem (apply.html); neue Blueprint-Route registriert in __init__.py; apply.html also Bewerbungsformular mit Nachricht + Budget erstellt | Ich habe einen Bug gefixt der sehr leicht zu übersehen war, __ name __ statt _ name _, und das in einer Stresssituation kurz vor der Abgabe.| Den Blueprint zu registrieren und debuggen - die Fehlermeldung zeigte auf die richtige Stelle aber der Grund war erst auf den zweiten Blick erkennbar.|
| 3 | Landing Page Designänderung (index.html + base.html); Fullscreen Hintergrund von Unsplash; Zentrierte Suchleiste direkt auf dem Bild; Zweispaltige Infosektion dadrunter (das wird noch bearbeitet + Kontaktformular), Stikcy Footer | Ich habe die base.html strukturell erweitert ohen andere Seiten kaputt zu machen. Das `{% raw %}{%block fullwidth%}{% endraw %}` war eine Lösung für das sich über die ganze Startseite erstreckendes Layout Problem. Ein normaler Bootstrap Container hat das Edge to Edge design verhindert.| Die Formatierung war die größte Hürde.Der Block fullwidth musste außerhalb des Containers platziert werden und der Sticky Footer hat sich nicht so verhalten wie erwartet. Beides erforderte sehr viel aufmerksamkeit.|

## Design Decisions that I led

1. [DD #02](../design-decisions/dd-02.md) 
2. [DD #03](../design-decisions/dd-03.md) 

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Trips-Suche + Filter + Detailseite (trips.py, trips.html, trip_detail.html) | 11b826e, c0787ee, 99ba461, 167593e, e11d931, 9d946da, 5ce11c7, d5911ec, 0579579, 9e6024f | SQLAlchemy Docs (Queries, ilike, JOIN), Flask Docs (request.args, session), DigitalOcean Flask-SQLAlchemy Tutorial (vollständige Links als kommentierte Quellenblöcke direkt in den jeweiligen Dateien) |
| Bewerbungssystem (apply.html, __init__.py, application.py): Bewerbungsformular mit Nachricht + Budget erstellt, Blueprint applications_bp registriert, __name__-Bug gefixt | 658ccf5 (Apply-Seite), bc75fab (Blueprint registriert), 9ea951e (Bug-Fix) a9628e75a1ce4fc01c8b2b7f9593dfbf39ab1715 | Flask Docs (Blueprints, Blueprint-Registrierung), Flask-Login (login_required), Flask-SQLAlchemy (get_or_404, insert), Flask Flashing)(vollständige Links als kommentierte Quellenblöcke direkt in den jeweiligen Dateien) |
| ContributionProof (git commits)Sources usedLanding Page Redesign (index.html, base.html): Fullscreen-Hero von Unsplash, zentrierte Suchleiste auf dem Bild | d78acc6, 3bdd5b1, e77ace5, 3ecb72b, 43e8506, f1c12c1, 6bfe55a | Bootstrap Docs (Grid, Utilities), MDN (Flexbox, background, positioning), W3Schools (padding), Unsplash (Bild) (vollständige Links als kommentierte Quellenblöcke direkt in den jeweiligen Dateien) |
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
