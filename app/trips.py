from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from .models import db, Trip, TravelStyle, Location
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
        location = request.form.get("location")
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
        



        destination = Location(name=location, city=location)
        db.session.add(destination)
        db.session.flush()

        
        trip = Trip(
            host_u_id=current_user.u_id,
            travel_style_id=int(travel_style_id),
            origin_id=destination.l_id,
            destination_id=destination.l_id,
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





@trips_bp.route("/trips")
def trips_list():
    destination = request.args.get("destination", "")
    continent = request.args.get("continent", "")
    travel_style_id = request.args.get("travel_style_id", "")
    budget_min = request.args.get("budget_min", "")
    budget_max = request.args.get("budget_max", "")
    start_date_str = request.args.get("start_date", "")
    
    query = Trip.query.join(Location, Trip.destination_id == Location.l_id)
     
    if destination:
        query = query.filter(Location.city.ilike(f"%{destination}%"))
    if continent:
        query = query.filter(Trip.continent == continent)
    if travel_style_id:
        query = query.filter(Trip.travel_style_id == int(travel_style_id))
    if budget_min:
        query = query.filter(Trip.budget_max >= int(budget_min))
    if budget_max:
        query = query.filter(Trip.budget_min <= int(budget_max))
    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        query = query.filter(Trip.start_date >= start_date)


    trips = query.all()
    travel_styles = TravelStyle.query.all()
    
    return render_template ("trips.html", 
            trips=trips, 
            destination=destination,
            continent=continent,
            travel_style_id=travel_style_id,
            budget_min=budget_min,
            budget_max=budget_max,
            start_date=start_date_str,
            continents=CONTINENTS,
            travel_styles=travel_styles,
            )


""" quellen
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
flask request                             https://www.geeksforgeeks .org/python/get-the-data-received-in-a-flask-request/
daten aus tabellen holen query join/all   https://docs.sqlalchemy.org/en/20/orm/queryguide/
operatoren wie .ilike()                   https://docs.sqlalchemy.org/en/20/core/operators.html#sqlalchemy.operators.ilike_op
tokyo iwo im namen suchen f"%{}           https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
string zu zahl umwandeln                  https://docs.python.org/3/library/functions.html#int
string zu datum umwandeln                 https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime

"""









@trips_bp.route("/api/trips", methods=["GET"])
def api_trips():
    #-> liefert die erstellten Trips als JSON zurück
    trips = Trip.query.all()
    result = []
    for trip in trips:
        result.append({
            "id": trip.t_id,
            "destination": trip.destination.city,
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