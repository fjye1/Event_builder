from flask import Blueprint, render_template

from app.forms import EventForm

home_bp = Blueprint('home', __name__)


@home_bp.route("/")
def index():
    form = EventForm()
    return render_template(
        "home/index.html",
        form=form)
