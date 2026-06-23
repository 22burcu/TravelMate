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
| 2 | Bewertungssystem (apply.html); neue Blueprint-Route registriert in __init__.py; apply.html also Bewerbungsformular mit Nachricht + Budget erstellt | Ich habe einen Bug gefixt der sehr leicht zu übersehen war, __ name __ statt _ name _, und das in einer Stresssituation kurz vor der Abgabe.| Den Blueprint zu registrieren und debuggen - die Fehlermeldung zeigte auf die richtige Stelle aber der Grund war erst auf den zweiten Blick erkennbar.|
| 3 | Landing Page Designänderung (index.html + base.html); Fullscreen Hintergrund von Unsplash; Zentrierte Suchleiste direkt auf dem Bild; Zweispaltige Infosektion dadrunter (das wird noch bearbeitet + Kontaktformular), Stikcy Footer | Ich habe die base.html strukturell erweitert ohen andere Seiten kaputt zu machen. Das {%block fullwidth%} war eine Lösung für das sich über die ganze Startseite erstreckendes Layout Problem. Ein normaler Bootstrap Container hat das Edge to Edge design verhindert.| Die Formatierung war die größte Hürde.Der Block fullwidth musste außerhalb des Containers platziert werden und der Sticky Footer hat sich nicht so verhalten wie erwartet. Beides erforderte sehr viel aufmerksamkeit.|

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md) Suchleiste auf der Landing Page statt auf der Navbar: Die Trip Suche wurde aus der Navbar entfernt und als zentrales Element auf der Landing Page platziert. Ein großes zentrales Suchelement kommuniziert sofort den Zweck der App. Bekannte Plattformen wie Airbnb oder Booking.com machen es genauso. Beweise in Trips.py, trips_list() ohne @login_required, apply() mit @login_required
2. [DD #01](../design-decisions/dd-01.md) Trip Suche ohne Login zugänglich: jeder kann Trips durchsuchen ohne ein Konto. Bewerben kann man sich aber nur wenn man ein Konto angelegt hat oder sich registriert hat. Dadurch hat man eine niedrige Einstiegshürde. Die Nutzer können die Plattform erst kennenlernen. Zu frühe Login Pflichten können Nutzer abschrecken. Beweis: trips.py, trips_list() ohne @login_required, apply() mit @login_required

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
