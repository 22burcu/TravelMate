from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
from flask_login import UserMixin


class User(db.Model, UserMixin): #https://coderivers.org/blog/how-to-make-a-website-with-python/
    #hier werden 2 Klassen geerbt, db.model sorgt für DB-Tabellen und UserMixin macht sie kompatible mit Flask-Login
    __tablename__ = "users" #tatsächliche tabellenname in der DB, sonst wird automatisch der Klassenname genommen
    u_id = db.Column(db.Integer, primary_key=True) #primary key, automatisch hochgezählt, muss nicht angegeben werden
    email = db.Column(db.String(255), nullable=False, unique=True) #Speichert die E-Mail-Adresse des Benutzers, muss eindeutig sein
    password_hash = db.Column(db.String(255), nullable=False) #Speichert den Hash des Passworts, nicht das Passwort selbst
    role = db.Column(db.String(10), nullable=False) # Speichert die Rolle des Benutzers (z.B. "host" oder "joiner")
    first_name = db.Column(db.String(255), nullable=False) # Speichert den Vornamen des Benutzers
    last_name = db.Column(db.String(255), nullable=False) # Speichert den Nachnamen des Benutzers
    birth_date = db.Column(db.Date, nullable=False) # Speichert das Geburtsdatum des Benutzers
    contact_info = db.Column(db.String(255)) # Speichert Kontaktdaten des Benutzers
    bio = db.Column(db.Text) # Speichert die Biografie des Benutzers
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now()) # Speichert das Erstellungsdatum des Benutzers, automatisch auf die aktuelle Zeit gesetzt

    trips = db.relationship('Trip', back_populates='host') # 
    applications = db.relationship('Application', back_populates='joiner')
    # 2 Virtuelle Spalten, die Reisen und Bewerbungen des Benutzers anzeigt, back_populates verknüpf es mit den gegenstück zu Trip und Application.
    # Das sind nur Python objekte und kein Datenbank feld

    def get_id(self):
        return str(self.u_id)
    
    
class TravelStyle(db.Model):
    __tablename__ = "travel_styles"
    ts_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    trips = db.relationship('Trip', back_populates='travel_style')
    # Virtuelle Spalte, die Reisen mit diesem Reisestil anzeigt, back_populates verknüpft es mit dem Gegenstück zu Trip.

class Location(db.Model):
    __tablename__ = "locations"
    l_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    # Virtuelle Spalten, die Reisen anzeigt, die diesen Ort als Startpunkt oder Ziel haben

    trips_as_origin = db.relationship('Trip', foreign_keys='Trip.origin_id', back_populates='origin') # gibt das Location-Obejkt zurück
    trips_as_destination = db.relationship('Trip', foreign_keys='Trip.destination_id', back_populates='destination') # gibt die Liste aller trips die Hier starten
    # db.relationship() wird verwendet, um eine Beziehung zwischen zwei Tabellen herzustellen, stattt selber die joins zu machen


class Trip(db.Model):
    __tablename__ = "trips"
    t_id = db.Column(db.Integer, primary_key=True) # t.id ist der Primärschlüssel
    host_u_id = db.Column(db.Integer, db.ForeignKey("users.u_id"), nullable=False) # fremdschlüssel, der auf die u_id in der users-Tabelle verweist
    travel_style_id = db.Column(db.Integer, db.ForeignKey("travel_styles.ts_id"), nullable=False) # fremdschlüssel, der auf die ts_id in der travel_styles-Tabelle verweist
    origin_id = db.Column(db.Integer, db.ForeignKey("locations.l_id"), nullable=False) # fremdschlüssel, der auf die l_id in der locations-Tabelle verweist                     
    destination_id = db.Column(db.Integer, db.ForeignKey("locations.l_id"), nullable=False) # fremdschlüssel, der auf die l_id in der locations-Tabelle verweist                         
    continent = db.Column(db.String(50), nullable=False) # Speichert den Kontinent, auf dem die Reise stattfindet | db.String verlangt das man eine länge angibt
    start_date = db.Column(db.Date, nullable=False) # Speichert das Startdatum der Reise                                                         
    end_date = db.Column(db.Date, nullable=False) # Speichert das Enddatum der Reise
    max_participants = db.Column(db.Integer, nullable=False) # Speichert die maximale Anzahl an Teilnehmern für die Reise
    budget_min = db.Column(db.Integer, nullable=False) # Speichert das minimale Budget für die Reise
    budget_max = db.Column(db.Integer, nullable=False) # Speichert das maximale Budget für die Reise
    description = db.Column(db.Text) # Speichert eine Beschreibung der Reise
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now()) # Speichert das Erstellungsdatum der Reise, automatisch auf die aktuelle Zeit gesetzt

    host = db.relationship('User', back_populates='trips')
    travel_style = db.relationship('TravelStyle', back_populates='trips')
    applications = db.relationship('Application', back_populates='trip')
    origin = db.relationship('Location', foreign_keys=[origin_id], back_populates='trips_as_origin')
    destination = db.relationship('Location', foreign_keys=[destination_id], back_populates='trips_as_destination')
    # die Beziehungen zwischen den Tabellen werden hier definiert

class Application(db.Model):
    __tablename__ = "applications" 
    a_id = db.Column(db.Integer, primary_key=True) # Application ID, Primärschlüssel
    trip_t_id = db.Column(db.Integer, db.ForeignKey("trips.t_id"), nullable=False) # trips_t_id ist welche reise der joiner sich bewirbt
    joiner_u_id = db.Column(db.Integer, db.ForeignKey("users.u_id"), nullable=False) # joiner_u_id ist der Benutzer, der sich bewirbt
    message = db.Column(db.Text) # Speichert eine Nachricht des Joiners
    budget_min = db.Column(db.Integer, nullable=False) # Speichert das minimale Budget für die Reise
    budget_max = db.Column(db.Integer, nullable=False) # Speichert das maximale Budget für die Reise
    status = db.Column(db.String(20), nullable=False, default='pending') # Speichert den Status der Bewerbung
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now()) # Speichert das Erstellungsdatum der Bewerbung, automatisch auf die aktuelle Zeit gesetzt

    trip = db.relationship('Trip', back_populates ='applications')
    joiner = db.relationship('User', back_populates = 'applications')
    # die Beziehungen zwischen den Tabellen werden hier definiert

    __table_args__ = (db.UniqueConstraint('trip_t_id', 'joiner_u_id', name='unique_application'),)
    # Das ist ein Tabellenweites regel, die sicherstellt, dass ein Joiner sich nur einmal pro Trip bewerben kann.


