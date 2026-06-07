from datetime import datetime

from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import db, User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registrierungs-Route"""

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birth_date_str = request.form.get("birth_date")

        if not all([email, password, confirm_password, first_name, last_name, birth_date_str]):
            return render_template("register.html", error="Alle Felder müssen ausgefüllt sein!")

        if password != confirm_password:
            return render_template("register.html", error="Passwörter stimmen nicht überein!")

        if User.query.filter_by(email=email).first():
            return render_template("register.html", error="Diese E-Mail ist bereits registriert!")

        try:
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            hashed_pw = generate_password_hash(password)

            new_user = User(
                email=email,
                password_hash=hashed_pw,
                role="user",
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
            )

            db.session.add(new_user)
            db.session.commit()

            flash("Konto erstellt! Bitte einloggen.", "success")
            return redirect(url_for('auth.login'))

        except Exception as e:
            db.session.rollback()
            return render_template("register.html", error=f"Fehler: {str(e)}")
        
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login-Route"""
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        if not email or not password:
            return render_template("login.html", error="E-Mail und Passwort erforderlich!")
        
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Erfolgreich eingeloggt!", "success")
            return redirect(url_for('main.index'))
        else:
            return render_template("login.html", error="Ungültige E-Mail oder Passwort!")
    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """Logout-Route"""

    logout_user()
    flash("Du wurdest abgemeldet!", "info")
    return redirect(url_for('main.index'))
