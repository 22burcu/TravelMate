from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
@login_required
def profile():
    """Profil anschauen"""
    return render_template("profile.html", user=current_user)

@profile_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    """Profil bearbeiten"""
    
    if request.method == "POST":
        bio = request.form.get("bio")
        contact_info = request.form.get("contact_info")
        
        current_user.bio = bio
        current_user.contact_info = contact_info
        
        db.session.commit()
        flash("Profil aktualisiert!", "success")
        return redirect(url_for("profile.profile"))
    
    return render_template("edit_profile.html", user=current_user)