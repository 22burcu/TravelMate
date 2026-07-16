from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Trip, db, Application
from datetime import date

dashboard_bp = Blueprint("dashboard", __name__) #Ein Blueprint ist wie ein Ordner für zusammengehörige Routen.

@dashboard_bp.route("/dashboard")
@login_required      #Nur eingeloggte Nutzer dürfen diese Seite aufrufen 

def host_dashboard():
        today = date.today()
        open_trips = Trip.query.filter(    # sucht alle Trips, die ..        
            Trip.host_u_id == current_user.u_id,          # vom aktuellen User gehostet werden 
            Trip.start_date > today                       # und deren Startdatum nach dem heutigen Datum liegt 
        ).all()                                           # .all() Gibt mir alle gefundenen Datensätze

        active_trips = Trip.query.filter(    # sucht alle Trips, die ..        
            Trip.host_u_id == current_user.u_id,         # vom aktuellen User gehostet werden
            Trip.start_date <= today,                    # bereits gestartet haben oder heute starten
            Trip.end_date >= today                       # noch nicht beendet sind
        ).all()
        past_trips = Trip.query.filter(   # sucht alle Trips, die ..
            Trip.host_u_id == current_user.u_id,         # vom aktuellen User gehostet werden
            Trip.end_date < today                        # bereits beendet sind
        ).all() 


        incoming_applications = Application.query.join(Trip).filter(   # Sucht alle Bewerbungen auf die eigenen Reisen des eingeloggten Hosts
            Trip.host_u_id == current_user.u_id       # Nur Trips des aktuellen Users
        ).all()

        return render_template("host_dashboard.html",         #Übergibt die geladenen Trips und Bewerbungen an das HTML-Template
                               open_trips=open_trips,         
                               active_trips=active_trips, 
                               past_trips=past_trips,
                               incoming_applications=incoming_applications)

@dashboard_bp.route("/dashboard/joiner")
@login_required

def joiner_dashboard():
    applications = Application.query.filter_by(  #sucht in der Applcation tabelle..
          joiner_u_id=current_user.u_id           # nur Bewerbungen, bei denen der eingeloggte Nutzer der Joiner ist
          ).all()
    
    return render_template("joiner_dashboard.html", applications=applications) #übergibt applications wert and html template

#-----------------------------------------------------------------------------
# QUELLEN
#-----------------------------------------------------------------------------
# current_user              https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
# SQLAlchemy Queries        https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/
#                           https://docs.sqlalchemy.org/en/20/orm/queryguide/