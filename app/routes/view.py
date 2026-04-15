from flask import Blueprint, render_template
from datetime import datetime
from app.forms import EventForm
from app.models import Event
from collections import defaultdict

view_bp = Blueprint('view', __name__)






@view_bp.route("/view")
def home():
    events = Event.query.order_by(Event.date.asc()).all()

    grouped = defaultdict(list)

    for event in events:
        summary = event.summary()

        grouped[event.date].append({
            "id": event.id,
            "name": summary["event_name"],
            "client": summary["client"],
            "venue": summary["venue"],

            # optional extras if you want them in UI later
            "products": summary["products"],
            "staff_count": len(summary["staff"]),
            "staff": summary["staff"],
        })

    grouped = dict(sorted(grouped.items()))

    return render_template("view/home.html", grouped=grouped)