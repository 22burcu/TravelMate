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
    #Auswahlliste für das Formular: Reisestile aus der DB, Kontinente aus fester Liste
    travel_styles = TravelStyle.query.all()

    if request.method == "POST":
        #Schritt 2 -> die notwendigen Formulardaten holen
        continent = request.form.get("continent")
        travel_style_id = request.form.get("travel_style_id")
        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")
        max_participants = request.form.get("max_participants")
        budget_min = request.form.get("budget_min")
        budget_max = request.form.get("budget_max")
        description = request.form.get("description")

        #Schritt 3: Die Datumsfelder in echte Date-Objekte umwandeln
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()           #Quelle: programiz.com

        #Schritt 4: Validierung der Bedingung
        if end_date < start_date:
            flash("Das Enddatum darf nicht vor dem Startdatum liegen.", "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        
        if int(budget_max) < int(budget_min):
            flash("Das maximale Budget darf nicht kleiner sein, als das minimale Budget", "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        
        #Schritt 5: Geschäftsregeln prüfen (max. 3 offene Trips, keine Überschneidungen!)
        allowed, error = can_host_create_trip(current_user.u_id, start_date, end_date)
        if not allowed:
            flash(error, "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        
        trip = Trip(
            host_u_id=current_user.u_id,
            travel_style_id=int(travel_style_id),
            location=location,
            continent=continent,
            start_date=start_date,
            end_date=end_date,
            max_participants=int(max_participants),
            budget_min=int(budget_min),
            budget_max=int(budget_max),
            description=description,
        )
        db.session.add(trip)
        db.session.commit()

        flash("Reise erfolgreich erstellt!", "success")
        #Platzhalter für später. Der User muss nach der erfolgreichen Erstellung wieder ins Dashboard zurück!
        return redirect(url_for("main.index"))
    
    return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)

@trips_bp.route("/api/trips", methods=["GET"])
def api_trips():
    #-> liefert die erstellten Trips als JSON zurück
    trips = Trip.query.all()
    result = []
    for trip in trips:
        result.append({
            "id": trip.t_id,
            "location": trip.location,
            "continent": trip.continent,
            "travel_style": trip.travel_style.name,
            "start_date": trip.start_date.isoformat(),   #Quelle: geeksforgeeks.com
            "end_date": trip.end_date.isoformat(),
            "max_participants": trip.max_participants,
            "budget_min": trip.budget_min,
            "budget_max": trip.budget_max,
            "description": trip.description,
        })
    return jsonify(result)