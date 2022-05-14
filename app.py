from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import folium

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


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

    return render_template("index.html", map=folium_map._repr_html_(), pricedb=Price.query.all(), scheduledb=Schedule.query.all())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Username: %r>" % self.username

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Name %r, Price: %r>' % (self.name, self.price)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.String(80), nullable=False)
    hours = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Days: %s, Hours %r>" % self.days, self.hours


if __name__ == "__main__":
    app.run(debug=True)
