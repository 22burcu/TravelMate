from app import create_app
from app.models import db, TravelStyle

app = create_app()

with app.app_context():


    db.drop_all()
    db.create_all()
    print("Datenbank-Tabellenn gelöscht und neu erstellt")


    # Vorgefertigte Reisestile legen wir als Stammdaten fest
    travel_styles = [
        TravelStyle(name="Backpacking"),
        TravelStyle(name="Kultur"),
        TravelStyle(name="Party"),
        TravelStyle(name="Luxus"),
        TravelStyle(name="Aktiv/Sport"),
        TravelStyle(name="Entspannung"),
        TravelStyle(name="Roadtrip"),
        TravelStyle(name="Foodie"),
    ]

    db.session.add_all(travel_styles)
    db.session.commit()
    print("Reisestile angelegt.")


    print("\nFertig! Datenbank ist initialisiert!")