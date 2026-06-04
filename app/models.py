from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"
    u_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    contact_info = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    trips = db.relationship('Trip', back_populates='host')
    applications = db.relationship('Application', back_populates='joiner')

    def get_id(self):
        return str(self.u_id)
    
class TravelStyle(db.Model):
    __tablename__ = "travel_styles"
    ts_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    trips = db.relationship('Trip', back_populates='travel_style')

class Location(db.Model):
    __tablename__ = "locations"
    l_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    trips_as_origin = db.relationship('Trip', foreign_keys='Trip.origin_id', back_populates='origin')
    trips_as_destination = db.relationship('Trip', foreign_keys='Trip.destination_id', back_populates='destination')



class Trip(db.Model):
    __tablename__ = "trips"
    t_id = db.Column(db.Integer, primary_key=True)
    host_u_id = db.Column(db.Integer, db.ForeignKey("users.u_id"), nullable=False)
    travel_style_id = db.Column(db.Integer, db.ForeignKey("travel_styles.ts_id"), nullable=False)
    origin_id = db.Column(db.Integer, db.ForeignKey("locations.l_id"), nullable=False)                           # Reiseziel = Startpunkt, wurde geändert, da es sonst zu Problemen mit der Datenbank kommt von (location = db.Column(db.String(255), nullable=False)) auf jetzigen version.
    destination_id = db.Column(db.Integer, db.ForeignKey("locations.l_id"), nullable=False)                            # aus fester Python-Liste, hier auch genau so.
    continent = db.Column(db.String(50), nullable=False)                                                         #Hier nochmal für herr Eck, bei mir in VSC gibt es fehler weswegen ich nicht committen kann.
    end_date = db.Column(db.Date, nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    budget_min = db.Column(db.Integer, nullable=False)
    budget_max = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    host = db.relationship('User', back_populates='trips')
    travel_style = db.relationship('TravelStyle', back_populates='trips')
    applications = db.relationship('Application', back_populates='trip')
    origin = db.relationship('Location', foreign_keys=[origin_id], back_populates='trips_as_origin')
    destination = db.relationship('Location', foreign_keys=[destination_id], back_populates='trips_as_destination')

class Application(db.Model):
    __tablename__ = "applications"
    a_id = db.Column(db.Integer, primary_key=True)
    trip_t_id = db.Column(db.Integer, db.ForeignKey("trips.t_id"), nullable=False)
    joiner_u_id = db.Column(db.Integer, db.ForeignKey("users.u_id"), nullable=False)
    message = db.Column(db.Text)
    budget_min = db.Column(db.Integer, nullable=False)
    budget_max = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    trip = db.relationship('Trip', back_populates ='applications')
    joiner = db.relationship('User', back_populates = 'applications')

    __table_args__ = (
        db.UniqueConstraint('trip_t_id', 'joiner_u_id', name='unique_application'),  # Ein Joiner kann sich pro Trip nur einmal bewerben
    )


