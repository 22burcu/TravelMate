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
    
    #Auswahlliste für das Formular: Reisestile aus der DB, Kontinente aus fester Liste
    travel_styles = TravelStyle.query.all()

    if request.method == "POST":
        #Schritt 2 -> die notwendigen Formulardaten holen
        location = request.form.get("location")
        continent = request.form.get("continent")
        travel_style_id = request.form.get("travel_style_id")
        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")
        max_participants = request.form.get("max_participants")
        budget_min = request.form.get("budget_min")
        budget_max = request.form.get("budget_max")
        description = request.form.get("description")
