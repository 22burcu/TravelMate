from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Trip, db, Application
from datetime import date

dashboard_bp = Blueprint("dashboard", __name__) #Ein Blueprint ist wie ein Ordner für zusammengehörige Routen.
@dashboard_bp.route("/dashboard")
@login_required      #Nur eingeloggte Nutzer dürfen diese Seite aufrufen 

def host_dashboard():
        today = date.today()
        open_trips = Trip.query.filter(            
            Trip.host_u_id == current_user.u_id,
            Trip.start_date > today
        ).all()  
        active_trips = Trip.query.filter(
            Trip.host_u_id == current_user.u_id,
            Trip.start_date <= today,
            Trip.end_date >= today
        ).all()
        past_trips = Trip.query.filter(
            Trip.host_u_id == current_user.u_id,
            Trip.end_date < today
        ).all() 


        incoming_applications = Application.query.join(Trip).filter(
            Trip.host_u_id == current_user.u_id
        ).all()

        return render_template("host_dashboard.html", open_trips=open_trips, active_trips=active_trips, past_trips=past_trips,incoming_applications=incoming_applications)

@dashboard_bp.route("/dashboard/joiner")
@login_required
def joiner_dashboard():
    applications = Application.query.filter_by(joiner_u_id=current_user.u_id).all()
    return render_template("joiner_dashboard.html", applications=applications)

#-----------------------------------------------------------------------------
# QUELLEN
#-----------------------------------------------------------------------------
# current_user              https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
# SQLAlchemy Queries        https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/
#                           https://docs.sqlalchemy.org/en/20/orm/queryguide/