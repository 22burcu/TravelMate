from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Application, Trip

applications_bp = Blueprint("applications", __name__)

@applications_bp.route("/trips/<int:trip_id>/apply", methods=["GET", "POST"])
@login_required
def apply(trip_id):
    # trip holen, 404 wenn nicht gefunden
    trip = Trip.query.get_or_404(trip_id)

    if request.method == "POST":
        # formulardaten holen
        message = request.form.get("message")
        budget_min = request.form.get("budget_min")
        budget_max = request.form.get("budget_max")

        # bewerbung erstellen und speichern
        application = Application(
            trip_t_id=trip_id,
            joiner_u_id=current_user.u_id,
            message=message,
            budget_min=int(budget_min),
            budget_max=int(budget_max),
            status="pending"
        )
        db.session.add(application)
        db.session.commit()

        flash("Bewerbung erfolgreich abgeschickt!", "success")
        return redirect(url_for("trips.trip_detail", trip_id=trip_id))

    return render_template("apply.html", trip=trip)

@applications_bp.route("/applications/<int:app_id>/accept", methods=["POST"])
@login_required
def accept_application(app_id):
    #Zuerst holen wir uns eine Bewerbung, sollte keine vorhanden sein kriegen wir eine Fehlermeldung
    application = Application.query.get_or_404(app_id)

    # Zweite Prüfung: Nur der Ersteller der Reise/Trip darf entscheiden ( Owner/Host check)
    if application.trip.host_u_id != current_user.u_id:
        flash("Du darfst nur Bewerbngen für deine eigenen Reisen bearbeiten", "danger")
        return redirect(url_for("dashboard.host_dashboard"))
    
# genutzte Quellen
# blueprint                       https://flask.palletsprojects.com/en/3.0.x/blueprints/
# @login_required                 https://flask-login.readthedocs.io/en/latest/#flask_login.login_required
# trip holen oder error           https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#get-or-404
# formulardaten holen             https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.form
# speichern in db                 https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#insert-update-delete
# erfolgsmeldung anzeigen         https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/
# weiterleiten nach absenden      https://flask.palletsprojects.com/en/3.0.x/api/#flask.redirect
