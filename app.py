from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route("/")
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

    return render_template("index.html", map=folium_map._repr_html_())


if __name__ == "__main__":
    app.run(debug=True)
