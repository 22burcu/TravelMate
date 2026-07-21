from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User

profile_bp = Blueprint("profile", __name__)   

@profile_bp.route("/profile")
@login_required

def profile():
    """Profil anschauen"""
    return render_template("profile.html", user=current_user) #übergibt current_user unter dem Namen user an das Template , damit die Profildaten angezeigt werden können.

@profile_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required

def edit_profile():
    """Profil bearbeiten"""
    
    if request.method == "POST":           # POST-Block: Wird nur ausgeführt, wenn das Formular abgeschickt wurde
        bio = request.form.get("bio")      # request.form enthält die vom HTML-Formular gesendeten Daten
        contact_info = request.form.get("contact_info") # .get() liest den Wert aus dem Formularfeld aus
        
        current_user.bio = bio
        current_user.contact_info = contact_info # Ersetzt die alte info des aktuell eingeloggten Users durch den neuen Wert,
                                                 # der vorher mit request.form.get() aus dem Formular ausgelesen wurde
        
        db.session.commit() # Speichert die Änderungen am User dauerhaft in der Datenbank.
        flash("Profil aktualisiert!", "success")
        return redirect(url_for("profile.profile")) #Nach dem Speichern zurück zur Profilansicht weiterleiten
    
    return render_template("edit_profile.html", user=current_user) #übergibt current_user unter dem Namen user an das Template

#-----------------------------------------------------------------------------
# QUELLEN
#-----------------------------------------------------------------------------
# Blueprint                 https://flask.palletsprojects.com/en/stable/blueprints/
# render_template           https://flask.palletsprojects.com/en/stable/api/#flask.render_template
# login_required            https://flask-login.readthedocs.io/en/latest/#flask_login.login_required
# current_user              https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
# HTTP-Methoden (GET/POST)  https://flask.palletsprojects.com/en/stable/quickstart/#http-methods
# request.form              https://flask.palletsprojects.com/en/stable/api/#flask.Request.form
# flash                     https://flask.palletsprojects.com/en/stable/patterns/flashing/
# redirect                  https://flask.palletsprojects.com/en/stable/api/#flask.redirect
# url_for                   https://flask.palletsprojects.com/en/stable/api/#flask.url_for
# Session commit            https://docs.sqlalchemy.org/en/20/orm/session_basics.html