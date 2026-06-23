TravelMate

TravelMate ist ein zweiseitiger Reise-Marktplatz. In der Host-Rolle erstellt man eigene Reisen und sucht Mitreisende, in der Joiner-Rolle durchsucht man bestehende Angebote und bewirbt sich auf passende Trips. Ein einzelnes Konto kann beide Rollen übernehmen, ein separater Account je Rolle ist nicht nötig.

Stack: Python · Flask · Jinja2 · Bootstrap 5 · SQLAlchemy · SQLite · Flask-Login
Voraussetzung: Python 3.10 oder neuer

Setup

Zuerst das Repository klonen:

bashgit clone https://github.com/22burcu/TravelMate.git
cd TravelMate

Danach die Umgebung einrichten und die App starten.

Windows:

batpython -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python create_db.py
python app.py

macOS / Linux:

bashpython3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python create_db.py
python app.py

Die App läuft anschließend auf http://127.0.0.1:5000 und lässt sich im Terminal mit Strg + C beenden.

Das Repository enthält bewusst keine Datenbank, da der Ordner instance/ über die .gitignore ausgeschlossen ist. create_db.py legt die SQLite-Datenbank lokal neu an und befüllt die Reisestile als Stammdaten. Die Anwendung startet deshalb mit leerer Datenbank – alle weiteren Inhalte entstehen im folgenden Ablauf.

Happy Path

Der gesamte Ablauf lässt sich mit einem einzigen Konto durchspielen. Dasselbe Konto erstellt zunächst eine Reise (Host-Rolle) und bewirbt sich anschließend auf eine Reise (Joiner-Rolle).


Auf http://127.0.0.1:5000 registrieren und mit den eben erstellten Daten einloggen.
Eine Reise erstellen unter http://127.0.0.1:5000/trips/new. Als Beispielwerte eignen sich Ziel Tokyo, Kontinent Asien, ein Reisestil nach Wahl, ein Zeitraum in der Zukunft, eine gewünschte Personenzahl und eine Budget-Range (z. B. 800–1500 €).
Die angebotenen Reisen unter http://127.0.0.1:5000/trips durchsuchen, optional nach Reiseziel filtern.
Eine Reise öffnen und über den Button „Bewerben" eine Bewerbung mit Nachricht und eigener Budget-Range abschicken.
Den Status der Bewerbung im Joiner-Dashboard unter http://127.0.0.1:5000/dashboard/joiner verfolgen.
Die eingegangene Bewerbung aus Host-Sicht im Dashboard unter http://127.0.0.1:5000/dashboard ansehen.


Damit ist der vollständige Ablauf abgedeckt: Registrierung, Reise erstellen, Reise finden, bewerben und den Status auf beiden Seiten nachvollziehen.

JSON-Schnittstelle

Die Anwendung stellt zusätzlich eine datenliefernde Schnittstelle ohne HTML bereit. Unter http://127.0.0.1:5000/api/trips werden alle Reisen als JSON ausgegeben.

Optional: Geschäftsregeln

Wer die Geschäftslogik prüfen möchte, kann als Host eine vierte gleichzeitig offene Reise anzulegen versuchen (wird wegen der Grenze von drei offenen Reisen abgelehnt) oder zwei Reisen mit überlappendem Zeitraum erstellen (wird ebenfalls abgelehnt).