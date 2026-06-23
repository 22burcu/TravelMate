from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Application, Trip

applications_bp = Blueprint("applications", _name_)

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
