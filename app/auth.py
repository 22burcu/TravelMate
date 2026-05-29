from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registrierungs-Route"""
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login-Route"""
    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """Logout-Route"""
    return redirect(url_for('main.index'))
