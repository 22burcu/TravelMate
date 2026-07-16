from datetime import datetime

from flask import Blueprint, request, render_template, redirect, url_for, flash #Flask Werkzeuge
from flask_login import login_user, login_required, logout_user, current_user   # 
from werkzeug.security import generate_password_hash, check_password_hash       # Für sichere Passwörter

from .models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"]) 
def register():
    """Registrierungs-Route"""

    # Wer schon eingeloggt ist, braucht kein Registrierungsformular
    # is_authenticated kommt von UserMixin (models.py)
    if current_user.is_authenticated:            
        return redirect(url_for('main.index'))
    
    if request.method == "POST":                # POST-Block: Wird nur ausgeführt, wenn das Formular abgeschickt wurde.

        email = request.form.get("email")                         # request.form ist ein Objekt, das Flask bereitstellt
        password = request.form.get("password")                   # enthält die vom HTML-Formular gesendeten
        confirm_password = request.form.get("confirm_password")   # verhält sich ähnlich wie ein Dictionary, aus dem man mit .get() einzelne Werte auslesen kann
        first_name = request.form.get("first_name")               # mit post werden die daten in request.form geschickt
        last_name = request.form.get("last_name")                 # jeder variable wird der wert aus dem formular  zugewiesen
        birth_date_str = request.form.get("birth_date")

        # Validierung 1: Alle Felder ausgefüllt?
        if not all([email, password, confirm_password, first_name, last_name, birth_date_str]): 
            return render_template("register.html",
                                    error="Alle Felder müssen ausgefüllt sein!") # render_template eingetippten Daten bleiben 

        # Validierung 2: Passwörter identisch bei pw Wiederholung?
        if password != confirm_password:
            return render_template("register.html", error="Passwörter stimmen nicht überein!")

        # Validierung 3: E-Mail schon vergeben? 
        # User.query               -> durchsucht die Tabelle "users"
        # .filter_by(email=email)  -> WHERE email = ... eingegebenen E-Mail im Formular
        # .first()                 -> ersten Treffer oder None
    
        if User.query.filter_by(email=email).first():
            return render_template("register.html", error="Diese E-Mail ist bereits registriert!")

        try: #Probier das ansonsten später except

            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date() 
            # string parse time: wandelt den String in ein datetime-Objekt
            # .date() schneidet Uhrzeit weg, wir wollen nur das Datum speichern

            hashed_pw = generate_password_hash(password, method="pbkdf2:sha256")
            # Das eingegebene Passwort wird mit der Methode pbkdf2:sha256 gehasht


            # Neues Objekt bauen mit hashed_pw und Datum im richtigen Format (datetime.date)
            new_user = User(
                email=email,
                password_hash=hashed_pw,     # nur der Hash, nie das Passwort
                role="user",                 # fest im Code, jeder ist "user"
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
            )

            db.session.add(new_user) # session.add() merkt sich das neue Objekt
            db.session.commit()      # commit() speichert es in der Datenbank. Erst ab hier hat new_user.u_id einen Wert.
       
            flash("Konto erstellt! Bitte einloggen.", "success")   # flash() legt die Nachricht in die Session -> überlebt den Redirect.
            return redirect(url_for('auth.login')) 
        
        # geht nur an wenn im try-Block etwas schiefgeht (failed Datenbank commit, falsches Datum-Format)
        # mit Exception werden alle Fehlerarten abgefangen
        # variable e enthält die Infos zum aufgetretenen Fehler
        except Exception as e:
            db.session.rollback()    # Ohne rollback bleibt die Session kaputt und JEDE weitere DB-Abfrage würde crashen, auch bei anderen Nutzern
                                     # rollback() setzt die Session zurück, damit sie wieder sauber ist.
            return render_template("register.html", error=f"Fehler: {str(e)}") # f klebt den Text "Fehler: " mit dem Inhalt von e zusammen
        
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login-Route"""
    
    if current_user.is_authenticated:              # Schon eingeloggt? Dann kein Login-Formular nötig
        return redirect(url_for('main.index'))        

    if request.method == "POST":
        email = request.form.get("email")          # request.form enthält die vom HTML-Formular per POST gesendeten Daten.
        password = request.form.get("password")    # Mit .get() werden die einzelnen Formularwerte ausgelesen und Python-Variablen zugewiesen.

        if not email or not password:
            return render_template("login.html", error="E-Mail und Passwort erforderlich!")
        
        # sucht in User Tabelle nach der E-Mail. Ergebnis: User-Objekt ODER None
        user = User.query.filter_by(email=email).first()

        # 1) Prüft, ob ein User mit der E-Mail in der DB existiert
        # 2) Vergleiche das eingegebene Passwort mit dem gespeicherten Passwort-Hash
        if user and check_password_hash(user.password_hash, password):
          
            login_user(user) # meldet den User an, speichert die User-ID in der Session/dem Cookie. current_user ist ab jetzt verfügbar.
            flash("Erfolgreich eingeloggt!", "success")
            return redirect(url_for('main.index'))
        
        else:
            # allgemeine Meldung für beide Fälle (E-Mail falsch / Passwort falsch).
            return render_template("login.html", error="Ungültige E-Mail oder Passwort!")
    return render_template("login.html")
                                    

@auth_bp.route("/logout")
@login_required  # prüft current_user.is_authenticated
def logout():
    """Logout-Route"""

    logout_user() 
    # Entfernt die User-ID aus der Session
    # Der Datensatz in der Datenbank bleibt bestehen

    flash("Du wurdest abgemeldet!", "info")
    return redirect(url_for('main.index'))



# ----------------------------------------------------------------------------
# QUELLEN
# ----------------------------------------------------------------------------
# Blueprints                https://flask.palletsprojects.com/en/3.0.x/blueprints/
# Formulardaten (request)   https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.form
# Passwort-Hashing          https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security
# Flask-Login               https://flask-login.readthedocs.io/en/latest/
# is_authenticated          https://flask-login.readthedocs.io/en/latest/#flask_login.UserMixin
# Flash-Nachrichten         https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/
# Datum parsen (strptime)   https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
# SQLAlchemy Queries        https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/
# all() Funktion            https://docs.python.org/3/library/functions.html#all
# logout                    https://flask-login.readthedocs.io/en/latest/