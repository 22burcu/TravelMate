from datetime import date
from .models import Trip


def get_host_open_trips(host_id):
    """Alle noch nicht abgelaufenen Trips eines Hosts (end_date >= heute)."""
    today = date.today()                                                
    return Trip.query.filter(
        Trip.host_u_id == host_id,
        Trip.end_date >= today
    ).all()


def date_ranges_overlap(start_a, end_a, start_b, end_b):
    """True, wenn sich zwei Zeiträume überschneiden."""
    return start_a <= end_b and start_b <= end_a


def can_host_create_trip(host_id, new_start, new_end):
    """
    Prüft die beiden Host-Regeln:
      1. Maximal 3 offene Trips gleichzeitig.
      2. Der neue Trip darf sich mit keinem bestehenden offenen Trip überschneiden.
    Rückgabe: (True, None) wenn erlaubt, sonst (False, Fehlermeldung).
    """
    open_trips = get_host_open_trips(host_id)

    # Regel 1: maximal 3 offene Trips
    if len(open_trips) >= 3:
        return False, "Du kannst maximal 3 offene Reisen gleichzeitig anbieten."

    # Regel 2: keine zeitliche Überschneidung mit bestehenden Trips
    for trip in open_trips:
        if date_ranges_overlap(new_start, new_end, trip.start_date, trip.end_date):
            return False, f"Die Reise überschneidet sich zeitlich mit deiner Reise nach {trip.destination.city}."

    return True, None

