from flask import Blueprint, render_template
from app.models import User

profile_bp = Blueprint('profile', __name__)


@profile_bp.route("/profile")
def home():

    user = User.query.first()  # temp until auth
    return render_template(
        "profile/home.html",user=user
        )