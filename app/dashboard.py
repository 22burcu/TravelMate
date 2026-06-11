from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Trip, db, Application

dashboard_bp = Blueprint("dashboard", __name__)
@dashboard_bp.route("/dashboard")
@login_required

@login_required
def dashboard():
        applications = Application.query.filter_by(joiner_u_id=current_user.u_id).all()
        today = date.today()
        open_trips = Trip.query.filter(
            Trip.host_u_id == current_user.u_id,
            Trip.end_date >= today
        ).all()   
