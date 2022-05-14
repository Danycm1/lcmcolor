import folium
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from website.database.models import Price, Schedule, User
from werkzeug.security import check_password_hash

views = Blueprint("views", __name__)


@views.route("/")
def home():
    folium_resize_map = folium.Figure(width=500, height=537)
    location = 49.16608033066788, 2.244747752531686

    folium_map = folium.Map(
        location,
        tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        attr="Google Maps",
        zoom_start=10,
    ).add_to(folium_resize_map)

    folium.Circle(location, radius=float(40 * 370)).add_to(folium_map)

    return render_template(
        "index.html",
        map=folium_map._repr_html_(),
        pricedb=Price.query.all(),
        scheduledb=Schedule.query.all(),
    )


@views.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.login"))


@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            print("dddd")
            return redirect(url_for("views.home"))
        else:
            flash('Le nom d\'utilisateur ou le mot de passe est incorrect.')

    return render_template("login.html", user=current_user)
