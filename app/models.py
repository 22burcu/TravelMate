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


class Trip(db.Model):
    __tablename__ = "trips"
    t_id = db.Column(db.Integer, primary_key=True)
    host_u_id = db.Column(db.Integer, db.ForeignKey("users.u_id"), nullable=False)
    travel_style_id = db.Column(db.Integer, db.ForeignKey("travel_styles.ts_id"), nullable=False)
    location = db.Column(db.String(255), nullable=False)                            # Reiseziel = Startpunkt
    continent = db.Column(db.String(50), nullable=False)                            # aus fester Python-Liste
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    budget_min = db.Column(db.Integer, nullable=False)
    budget_max = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    host = db.relationship('User', back_populates='trips')
    travel_style = db.relationship('TravelStyle', back_populates='trips')
    applications = db.relationship('Application', back_populates='trip')

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


