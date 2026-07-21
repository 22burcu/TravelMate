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

1. [DD #04](../design-decisions/dd-04.md)
2. [DD #05](../design-decisions/dd-05.md)
 
---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Authentifizierungsflow (Register, Login, Logout) |  [add auth blueprint structure](https://github.com/22burcu/TravelMate/commit/e6bf7b95a46d847b407dc7605ff7e0c2eed8d68a), [user registration logic](https://github.com/22burcu/TravelMate/commit/38c94a433319228f126ab8e98a46b5ca186e2092), [add registration page](https://github.com/22burcu/TravelMate/commit/2b8ff478a8f5369eb13be41fb1c3383887c6274b), [simplify registration process](https://github.com/22burcu/TravelMate/commit/bfbc84eb58cb96f4ab8000875b70ad1aee81184a), [add login page](https://github.com/22burcu/TravelMate/commit/9c14133dcef15c97ccd97fee3e3fae343ee9cb34), [implement login and logout](https://github.com/22burcu/TravelMate/commit/dc5e308da99d049ca3b468da9d589783b1cb9410) | [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/), [Werkzeug Documentation](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.generate_password_hash), [DigitalOcean Flask-Login Tutorial](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-de), [GeeksforGeeks Flask Request](https://www.geeksforgeeks.org/html/retrieving-html-from-data-using-flask/), [iditect.com current_user](https://www.iditect.com/faq/python/how-to-check-if-a-user-is-logged-in-how-to-properly-use-userisauthenticated-in-python.html), [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/), [Flask Flash-Nachrichten](https://flask.palletsprojects.com/en/stable/patterns/flashing/), [Flask redirect()](https://flask.palletsprojects.com/en/stable/api/#flask.redirect), [Flask url_for()](https://flask.palletsprojects.com/en/stable/api/#flask.url_for), [Python datetime strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime), [Flask-SQLAlchemy Queries](https://flask-sqlalchemy.palletsprojects.com/en/stable/queries/), [SQLAlchemy Session commit/rollback](https://docs.sqlalchemy.org/en/20/orm/session_basics.html), [Python all()](https://docs.python.org/3/library/functions.html#all) |
| Profilsystem (Profil anzeigen und bearbeiten)|  [add profile blueprint](https://github.com/22burcu/TravelMate/commit/441b900be9e324fab646d56986f60644feffa81a), [add profile edit route](https://github.com/22burcu/TravelMate/commit/a353f0f84e24c8dd772304328b8ccab4a156fc4b), [add profile navigation link](https://github.com/22burcu/TravelMate/commit/34e029ea5ae5141c88f23455966bac926b3d3284), [create user profile page](https://github.com/22burcu/TravelMate/commit/f81f4994e4d103f08644530a7bdd772dfd17be3e), [add bio and contact info form](https://github.com/22burcu/TravelMate/commit/99989441b85bb4b3cdd3084b66af56820bed3786), [add profil edit buttons](https://github.com/22burcu/TravelMate/commit/1b359550f3cf406ba966c4dbde7f2d333d41b7e1) | [Jinja2 Template Inheritance](https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance), [Jinja2 Filters (upper)](https://jinja.palletsprojects.com/en/stable/templates/#filters), [Jinja2 or-Operator/Math](https://jinja.palletsprojects.com/en/stable/templates/#math), [Flask url_for()](https://flask.palletsprojects.com/en/stable/api/#flask.url_for), [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/), [Flask Routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing), [Flask HTTP-Methoden (GET/POST)](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods), [Flask request.form](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form), [Flask flash()](https://flask.palletsprojects.com/en/stable/api/#flask.flash), [Flask redirect()](https://flask.palletsprojects.com/en/stable/api/#flask.redirect), [Flask-Login (login_required, current_user)](https://flask-login.readthedocs.io/en/latest/#flask_login.login_required), [Flask-Login Übersicht](https://flask-login.readthedocs.io/en/latest/), [Flask-SQLAlchemy Models](https://flask-sqlalchemy.palletsprojects.com/en/stable/models/), [Flask-SQLAlchemy Quickstart](https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/), [Flask-SQLAlchemy db.session.commit()](https://flask-sqlalchemy.palletsprojects.com/en/stable/queries/), [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/), [Bootstrap Flex Utilities](https://getbootstrap.com/docs/5.3/utilities/flex/), [Bootstrap Buttons](https://getbootstrap.com/docs/5.3/components/buttons/), [Bootstrap Block-Buttons (d-grid)](https://getbootstrap.com/docs/5.3/components/buttons/#block-buttons), [Bootstrap Sizing (rounded-circle, mx-auto)](https://getbootstrap.com/docs/5.3/utilities/sizing/), [Bootstrap Forms](https://getbootstrap.com/docs/5.3/forms/overview/), [Python datetime strftime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes), [MDN HTML Forms (POST)](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form) |
| Host/Joiner Dashboard Split | [Separate host/joiner dashboard views](https://github.com/22burcu/TravelMate/commit/4188da9bc04bd158b6e686dc08c33f3ebaa68073), [add host dashboard template](https://github.com/22burcu/TravelMate/commit/c29fb036c6e50c8b94186c77fbbc26adb850363e), [add joiner dashboard template](https://github.com/22burcu/TravelMate/commit/719fc36c254656c55a9f46c025385cf81f3887c5), [add navbar links](https://github.com/22burcu/TravelMate/commit/23062e69b7ebf1260a6255f13f550bf8193f1657)| [Jinja2 Templates (Vererbung, Schleifen)](https://jinja.palletsprojects.com/en/stable/templates/), [Jinja2 Variablen & Attributzugriff](https://jinja.palletsprojects.com/en/stable/templates/#variables), [Flask Quickstart (url_for, Routing)](https://flask.palletsprojects.com/en/stable/quickstart/), [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/), [Flask-Login](https://flask-login.readthedocs.io/en/latest/), [Bootstrap Containers](https://getbootstrap.com/docs/5.3/layout/containers/), [Bootstrap Grid](https://getbootstrap.com/docs/5.3/layout/grid/), [Bootstrap Buttons](https://getbootstrap.com/docs/5.3/components/buttons/), [Bootstrap Spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/), [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/), [Bootstrap Borders](https://getbootstrap.com/docs/5.3/utilities/borders/), [Bootstrap Colors](https://getbootstrap.com/docs/5.3/utilities/colors/), [Bootstrap Alerts](https://getbootstrap.com/docs/5.3/components/alerts/), [Bootstrap Tables](https://getbootstrap.com/docs/5.3/content/tables/), [Bootstrap Badges](https://getbootstrap.com/docs/5.3/components/badge/), [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/), [SQLAlchemy Query Guide (Filter, Joins)](https://docs.sqlalchemy.org/en/20/orm/queryguide/), [Python datetime (date.today)](https://docs.python.org/3/library/datetime.html#datetime.date.today),[Flask render_template()](https://flask.palletsprojects.com/en/stable/api/#flask.render_template) |
|  |  |  |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Perplexity AI | Profilkreis mit Initialien | Profile.py, profil.html | [Profilkreis](assests/pdf/Profilkreis_mit_Initialien.pdf)                             |
| 02  | Perplexity AI | Fehler im Code auffangen damit Seite nicht crashed | auth.py | [ty-except](assets/pdf/Try_except.pdf) |
| 03  | ChatGpt | Wie sucht man User in der DB | auth.py | [Benutzersuche](assets/pdf/Benutzersuche_in_DB.pdf) |
| 04  | ChatGpt | Einladung auf github für Repository schickt | --- | [Contributer einladen](assets/pdf/Repository_Einladen.pdf) |
| 05  | ChatGpt | Repository setup | --- | [Repo setup](assets/pdf/GitHub_Repository_klonen.pdf) |
| 06  | ChatGpt | Wie man im Markdown Text formatiert | Individual Contribution, Design Decisions | [Markdown Formatierung](assets/pdf/Markdown_Stichpunkte.pdf) |
| 07  | Perplexity AI | Fehler finden im html Code | host_dashbord.html | [Fehler finden](assets/pdf/Fehlermeldung_Dashboard.pdf)|
| 08  | Perplexity AI | Nach Bewerbungen filtern, die der Host erhält| dashboard.py | [Bewerbungen filtern](assets/pdf/Bewerbungen_filtern.pdf) |
| 09  |         |                |                                 |                             |
