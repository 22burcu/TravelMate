from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify, session #request liest http dateien die der browser an den server schickt, zb ausfüllen von formularen durch den nutzer
from flask_login import login_required, current_user
from datetime import datetime
from .models import db, Trip, TravelStyle, Location
from .constants import CONTINENTS
from .business_rules import can_host_create_trip

trips_bp = Blueprint("trips", __name__) #blueprint=bauplan, aus bib flask ->zusammenhängende funktionen übersichtlich organisieren
#trips_bp ist ein blueprint objekt      #trips_bp ist eine variable die eine blueprint instanz speichert
#und besitzt eine methode route()       #blueprint(..) ist konstruktor -> so wird ein blueprint objekt erzeugt
#deswegeen vordefinieren nicht notwendig#"trips" hilf flask den routen eindeutig zu erkennen
#route() nicht von uns definiert sondern methode in klasse blueprint vorprogrammiert

#registriert die url beim trips blueprint und registriert die funktion als route
@trips_bp.route("/trips/new", methods=["GET", "POST"])  #decorator-erweiter oder verändert das verhalten einer funktion
@login_required     #ohne methods= gilt standardmäßig nur get ohne post #wenn jemand die url abruft soll die funktion ausgeführt werden                 
def create_trip():    #definition einer funktion
    #Auswahlliste für das Formular: Reisestile aus der DB, Kontinente aus fester Liste
    travel_styles = TravelStyle.query.all() #TravelSytles ist die python-repräsentation eines datenbankmodells
                                            #alle reisestille aus der datenbank holen damit die zur auswhal stehen 

    if request.method == "POST": #liest formulardaten, prüft, speichert,zeigt erfolgsmeldung, zurück zur startseite
        #request liest http-anfragen des browsers die an den server gesendet werden 
        location = request.form.get("location")    #request.form.get() die einzelnen eingaben des benutzers aus dem html fomrular auslesen
        continent = request.form.get("continent")  #kommen nicht aus datenbank sondern festen python datei
        travel_style_id = request.form.get("travel_style_id") #weil kontinente konstant sind und reisestile
        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")
        max_participants = request.form.get("max_participants")
        budget_min = request.form.get("budget_min")
        budget_max = request.form.get("budget_max")
        description = request.form.get("description") 


        #nachdem benutzer das formular abgeschickt hat und flaks werte ausgelesen hat 
        #die eingegebenen daten werden überprüft und in die richtige datentypen umgewandelt
        try:                     #ist eine fehlerbehandlung - exception handling-falls 
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() #.strptime() wandelt string in datum um-so kann db vergleichen
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()   #.date() entfernt die uhrzeit kompletten datum zeit objekt
            travel_style_id = int(travel_style_id) #formular string aber in db abgespeichert mit int
            max_participants = int(max_participants) #aus "5" wird int
            budget_min = int(budget_min)
            budget_max = int(budget_max)
        except (ValueError, TypeError): #falsch eingetragen durch user -> diese meldung
            flash("Bitte gib gültige Werte ein.", "danger")
            return render_template(    #formular wird neu angezeigt- render_templ-lädt das html template
                "create_trip.html",    #durch aufbau html datei wird das gleiche fomular nochmal angezeigt
                travel_styles=travel_styles,    #links name unter dem html die daten bekommt, rechts python variable
                continents=CONTINENTS       #muss eingegeben werden weil es nicht über reuest.form zurück kommt
            ) 


        #validierung der Bedingung-also macht die eingabe überhaupt sinn??
        if end_date < start_date:
            flash("Das Enddatum darf nicht vor dem Startdatum liegen.", "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        
        if (budget_max) < (budget_min):
            flash("Das maximale Budget darf nicht kleiner sein, als das minimale Budget", "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        


        #prüfung der geschäftsregeln business rules
        allowed, error = can_host_create_trip(current_user.u_id, start_date, end_date) #funktion kommt aus business rules py
        if not allowed:
            flash(error, "danger")
            return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS)
        



        destination = Location(name=location, city=location) #macht aus der eingabe datenbankobjekt
        db.session.add(destination) #speichert neues objekt
        db.session.flush()  #erstellt location id damit der trip mit der richtigen location verknüpft werden kann

        
        #hier wird der trip endgültig erstellt
        trip = Trip(            #trip objekt erstellen-reisedaten werden zu trip objekt
            host_u_id=current_user.u_id,    #wer ist der ersteller? current user importiert vom flask login
            travel_style_id=int(travel_style_id),   
            origin_id=destination.l_id,     #
            destination_id=destination.l_id,
            continent=continent,
            start_date=start_date,
            end_date=end_date,
            max_participants=int(max_participants),
            budget_min=int(budget_min),
            budget_max=int(budget_max),
            description=description,
        )
        db.session.add(trip)    #fügt den neuen trip zur datenbank session hinzu, noch nicht entgültig gespeichert 
        db.session.commit()     #hierdurch entgültig gespeichert

        flash("Reise erfolgreich erstellt!", "success")
        return redirect(url_for("dashboard.host_dashboard")) 
    
    return render_template("create_trip.html", travel_styles=travel_styles, continents=CONTINENTS) #wenn user seite zum ersten mal aufruft


''' quellen
blueprint                     		    https://flask.palletsprojects.com/en/3.0.x/blueprints/
route decorator + methods     		    https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.route
@login_required               		    https://flask-login.readthedocs.io/en/latest/#flask_login.login_required
current_user                  		    https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
formulardaten auslesen        		    https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.form
query.all()                   		    https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#select
datetime.strptime             		    https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
.date() aus datetime          		    https://docs.python.org/3/library/datetime.html#datetime.datetime.date
int() typumwandlung           		    https://docs.python.org/3/library/functions.html#int
try/except fehlerbehandlung   		    https://docs.python.org/3/tutorial/errors.html#handling-exceptions
ValueError                    		    https://docs.python.org/3/library/exceptions.html#ValueError
TypeError                     		    https://docs.python.org/3/library/exceptions.html#TypeError
flash nachrichten             		    https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/
render_template               		    https://flask.palletsprojects.com/en/3.0.x/api/#flask.render_template
if bedingung / vergleich      		    https://docs.python.org/3/tutorial/controlflow.html#if-statements
neues objekt erstellen und hinzufügen   https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#insert-update-delete
flush() id vor commit holen   		    https://docs.sqlalchemy.org/en/20/orm/session_basics.html#flushing
commit() endgültig speichern  		    https://docs.sqlalchemy.org/en/20/orm/session_basics.html#committing
weiterleiten nach dem erstellen         https://flask.palletsprojects.com/en/3.0.x/api/#flask.redirect
url_for                                 https://flask.palletsprojects.com/en/3.0.x/api/#flask.url_for
'''



@trips_bp.route("/trips")       #trips suchen filtern und anzeigen 
def trips_list():
    destination = request.args.get("destination", "")       #FILTER aus der url lesen -request.args.get()
    continent = request.args.get("continent", "")           #""wenn nicht angegeben wurd enimm einen leeren string
    travel_style_id = request.args.get("travel_style_id", "")
    budget_min = request.args.get("budget_min", "")
    budget_max = request.args.get("budget_max", "")
    start_date_str = request.args.get("start_date", "")
    end_date_str = request.args.get("end_date", "") 
    
    query = Trip.query.join(Location, Trip.destination_id == Location.l_id) #datenbankabfrage-hole trips und verbinde sie mit der locationtabelle
                                                                            #weil mein trip nur eine id speichert aber ich nach tokyo suche
                                                                            #1 id tokyo city deswegen sql alchemy verbindung um beide spalten abzulesen
    if destination:
        query = query.filter(Location.city.ilike(f"%{destination}%"))       #%..% irgnedwo im text kommt toyko vor
    if continent:                                                           #ilike groß kleinschriebung ignoriert
        query = query.filter(Trip.continent == continent)                   #sql filter WHERE ==
    if travel_style_id:
        query = query.filter(Trip.travel_style_id == int(travel_style_id))  #int weil url wert text aber db int
    if budget_min:
        query = query.filter(Trip.budget_max >= int(budget_min))        #min 500? dann zeige reisen mit maximum mindestens 500
    if budget_max:
        query = query.filter(Trip.budget_min <= int(budget_max))
    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()   #in Datum(...,..,..) umwandeln 
        query = query.filter(Trip.start_date >= start_date)                 #zeige reisen die ab diesem datum beginnen
    if end_date_str:                                                       
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()       
        query = query.filter(Trip.end_date <= end_date)                     

    trips = query.all()         #führt die suche aus - sql abfrage an db senden
    travel_styles = TravelStyle.query.all()     #wieder extra weil es ein dropdown ist
    
    session['last_list_url'] = request.url
    return render_template ("trips.html",       #jz wird die seite geöffnet 
            trips=trips,                        #gefundene reisen
            destination=destination,            #aktuelle filterwerte behalten
            continent=continent,                
            travel_style_id=travel_style_id,
            budget_min=budget_min,
            budget_max=budget_max,
            start_date=start_date_str,
            end_date=end_date_str,             
            continents=CONTINENTS,              #dropdown anzeigen
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
session speichern                         https://flask.palletsprojects.com/en/3.0.x/api/#flask.session
vollständige url der anfrage              https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.url
ki quelle session get zurück button im ki quellenverzeichnis
"""



@trips_bp.route("/trips/<int:trip_id>") #erwartet trip id in der url
def trip_detail(trip_id):               # trip anhand der id aus der db holen, 404 wenn nicht gefunden
    trip = Trip.query.get_or_404(trip_id)
    return render_template("trip_detail.html", trip=trip)   #html seite öffnen und gefunden trip wird an html template übergeben


""" quellen
url parameter <int:trip_id>     https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
trips holen oder error          https://flask-sqlalchemy.palletsprojects.com/en/stable/queries/#get-or-404
"""



@trips_bp.route("/trips/<int:trip_id>/delete", methods=["POST"])
@login_required
def delete_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    if trip.host_u_id != current_user.u_id:
        flash("Du kannst nur deine eigenen Reisen löschen.", "danger")
        return redirect(url_for("dashboard.host_dashboard"))

    # zugehörige Bewerbungen zuerst löschen, sonst Foreign-Key-Fehler
    for application in trip.applications:
        db.session.delete(application)

    db.session.delete(trip)
    db.session.commit()
    flash("Reise gelöscht.", "info")
    return redirect(url_for("dashboard.host_dashboard"))


''' quellen
YouTube datenbankeinträge löschen 	    https://www.youtube.com/watch?v=7jKsHOZk-IE
Youtube datenbankeinträge löschen	    https://www.youtube.com/watch?v=y4ua8SsT0So
trip holen oder 404                     https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#queries-for-views
route mit POST methode                  https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.route
owner check vor dem löschen             https://flask.palletsprojects.com/en/3.0.x/patterns/viewdecorators/
objekt aus db löschen delete()          https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#insert-update-delete
verknüpfte daten über relationship      https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship
for schleife über liste                 https://docs.python.org/3/tutorial/controlflow.html#for-statements
commit endgültig speichern              https://docs.sqlalchemy.org/en/20/orm/session_basics.html#committing
weiterleiten redirect                   https://flask.palletsprojects.com/en/3.0.x/api/#flask.redirect
'''



@trips_bp.route("/api/trips", methods=["GET"]) 
def api_trips():      #api schnittstelle über die programme daten austauschen
   
    trips = Trip.query.all()    #holt alle trips aus db
    result = []     #leere liste damit da später alle reisen rein können
    for trip in trips:      #gehe jede reise durch
        result.append({     #es wird für jede reise ein neuer eintrag zur liste hinzugefügt
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
    return jsonify(result) # in json weil apps, webseiten javascript und anderee server es leicht lesen können


''' quellen
json mit flask für api zurückgeben	    https://www.youtube.com/watch?v=Up5Gm_Ls2oQ
was ist eine REST api                   https://developer.mozilla.org/en-US/docs/Glossary/REST
route mit GET methode                   https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.route
alle trips aus db holen query.all()     https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#select
liste erstellen und append()            https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
for schleife über objekte               https://docs.python.org/3/tutorial/controlflow.html#for-statements
dictionary aufbau key value             https://docs.python.org/3/tutorial/datastructures.html#dictionaries
datum in string isoformat()             https://docs.python.org/3/library/datetime.html#datetime.date.isoformat
jsonify json-antwort zurückgeben        https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify
was ist json                            https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON
'''
