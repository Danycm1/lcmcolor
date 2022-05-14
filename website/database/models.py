from flask_login import UserMixin
from website import db


class User(db.Model, UserMixin):
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
        return "<Name %r, Price: %r>" % (self.name, self.price)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.String(80), nullable=False)
    hours = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Days: %s, Hours %r>" % self.days, self.hours
