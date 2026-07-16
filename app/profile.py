from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User

profile_bp = Blueprint("profile", __name__)   #Ein Blueprint ist wie ein Ordner für zusammengehörige Routen

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