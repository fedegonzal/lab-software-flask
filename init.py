import os
import csv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'universities.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# University Model
class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(200), nullable=True)
    website = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)

    def __init__(self, name, address, city, state, country, picture, website, lat, lng):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.picture = picture
        self.website = website
        self.lat = lat
        self.lng = lng

# University Schema
class UniversitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = University
        load_instance = True

# Seed the database with real data from CSV
def seed_db():
    if University.query.count() == 0:
        csv_file_path = os.path.join(basedir, 'seed.csv')
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                university = University(
                    name=row['name'],
                    address=row['address'],
                    city=row['city'],
                    state=row.get('state', ''),
                    country=row['country'],
                    picture=row.get('picture', ''),  # Assume picture URL is optional
                    website=row['website'],
                    lat=float(row['lat']) if row['lat'] else None,
                    lng=float(row['lng']) if row['lng'] else None
                )
                db.session.add(university)
            db.session.commit()

# Initialize schemas
university_schema = UniversitySchema()
universities_schema = UniversitySchema(many=True)

# Create the database
with app.app_context():
    seed_db()
