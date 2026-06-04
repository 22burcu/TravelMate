from flask import Blueprint, app, request, jsonify
from .trips import trips_bp
from .models import db, Trip, Location

trips_bp = Blueprint("trips", __name__)
app.register_blueprint(trips_bp)


