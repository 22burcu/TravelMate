from flask import Blueprint, request, jsonify
from .models import db, Trip

trips_bp = Blueprint("trips", __name__)

@trips_bp.route("/api/trips", methods=["POST"])
def create_trip():
    data = request.get_json()

    trip = Trip(
        host_u_id=data['user_id'],
        travel_style_id=data['travel_style_id'],
        location=data['location'],
        continent=data['continent'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        max_participants=data['max_participants'],
        budget_min=data['budget_min'],
        budget_max=data['budget_max'],
        description=data['description']
    )
    db.session.add(trip)
    db.session.commit()

    return jsonify({"message": "Trip created successfully"}), 201