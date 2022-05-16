import folium
from flask import Blueprint, render_template
from website.database.models import Price, Schedule

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
