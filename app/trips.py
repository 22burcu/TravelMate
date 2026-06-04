from flask import Blueprint, request, jsonify
from .models import db, Trip, Location

trips_bp = Blueprint("trips", __name__)



