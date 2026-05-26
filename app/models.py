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
    caontact_info = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    trips = db.relationships('Trip', back_populates='host')
    applications = db.relationship('Application', back_populates='joiner')

    def get_id(self):
        return str(self.u_id)
    

    