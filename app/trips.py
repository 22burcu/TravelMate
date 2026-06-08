from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from .models import db, Trip, TravelStyle
from .constants import CONTINENTS
from .business_rules import can_host_create_trip

trips_bp = Blueprint("trips", __name__)

@trips_bp.route("/trips/new", methods=["GET", "POST"])
@login_required                                                         
def create_trip():
    # Schritt 1: Nur Hosts dürfen Reisen erstellen
    if current_user.role != "host":
        flash("Nur Hosts können Reisen erstellen.", "danger")
        return redirect(url_for("main.index"))