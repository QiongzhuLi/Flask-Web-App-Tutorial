from flask import Blueprint , render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')   ##It is a decorator, which means whenever you go to this route, the following function will run
@login_required   ## login required, see __init__.py
def home():
    return render_template("home.html", user=current_user)