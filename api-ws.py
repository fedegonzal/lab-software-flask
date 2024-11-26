import os
import csv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_sock import Sock
from flask_cors import CORS
import json

# Initialize web server
app = Flask(__name__)
CORS(app) # Enable CORS to allow requests from any origin

# base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize websocket server
sock = Sock(app)

# List of connected clients
clients = []

# We want to notify all clients when a new event is created
def notify_clients(message):
    message = json.dumps(message)
    for client in clients:
        client.send(message)


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

# Routes

# Get all universities
@app.route('/universities', methods=['GET'])
def get_universities():
    all_universities = University.query.all()
    return universities_schema.jsonify(all_universities)

# Get a single university by ID
@app.route('/universities/<int:id>', methods=['GET'])
def get_university(id):
    university = University.query.get(id)
    if university is None:
        return jsonify({"message": "University not found"}), 404
    return university_schema.jsonify(university)



# Create a new university
@app.route('/universities', methods=['POST'])
def add_university():
    data = request.json
    university = University(
        name=data.get('name'),
        address=data.get('address'),
        city=data.get('city'),
        state=data.get('state'),
        country=data.get('country'),
        picture=data.get('picture'),
        website=data.get('website'),
        lat=data.get('lat'),
        lng=data.get('lng')
    )
    db.session.add(university)
    db.session.commit()

    # convert the object to JSON
    json_data = university_schema.dump(university)

    # Notify all clients
    notify_clients({'action': 'CREATE', 'data': json_data})

    return json_data, 201


# Update an existing university by ID
@app.route('/universities/<int:id>', methods=['PUT'])
def update_university(id):
    university = University.query.get(id)

    if university is None:
        return jsonify({"message": "University not found"}), 404

    data = request.json
    university.name = data.get('name', university.name)
    university.address = data.get('address', university.address)
    university.city = data.get('city', university.city)
    university.state = data.get('state', university.state)
    university.country = data.get('country', university.country)
    university.picture = data.get('picture', university.picture)
    university.website = data.get('website', university.website)
    university.lat = data.get('lat', university.lat)
    university.lng = data.get('lng', university.lng)

    db.session.commit()

    # convert the object to JSON
    json_data = university_schema.dump(university)

    # Notify all clients
    notify_clients({'action': 'UPDATE', 'data': json_data})

    return json_data


# Delete a university by ID
@app.route('/universities/<int:id>', methods=['DELETE'])
def delete_university(id):
    university = University.query.get(id)
    if university is None:
        return jsonify({"message": "University not found"}), 404

    db.session.delete(university)
    db.session.commit()

    # convert the object to JSON
    json_data = university_schema.dump(university)

    # Notify all clients
    notify_clients({'action': 'DELETE', 'data': json_data})

    return jsonify({"message": "University deleted successfully"})


# WebSocket Route (for real-time notifications)
@sock.route('/ws')
def websocket(ws):
    clients.append(ws)
    try:
        while True:
            ws.receive()  # We simply listen, no need to process data
    finally:
        clients.remove(ws)



# Run the server
if __name__ == '__main__':

    # Initialize schemas
    university_schema = UniversitySchema()
    universities_schema = UniversitySchema(many=True)

    app.run(debug=True)
