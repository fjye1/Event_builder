from datetime import datetime
from app.extensions import db

# ------------------
# User
# ------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationships
    events = db.relationship('Event', backref='created_by', lazy=True)

# ------------------
# Company
# ------------------
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    # One-to-many: a company can have multiple clients
    clients = db.relationship('Client', backref='company', lazy=True)


# ------------------
# Client
# ------------------
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(50))

    # Optional link to a company
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)

    # Many-to-many with venues (via association table)
    venues = db.relationship(
        'Venue',
        secondary='venue_clients',
        back_populates='clients'
    )

    # Optional link to events
    events = db.relationship('Event', backref='client_ref', lazy=True)


# Association table for many-to-many between Venue and Client
venue_clients = db.Table(
    'venue_clients',
    db.Column('venue_id', db.Integer, db.ForeignKey('venue.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'))
)


# ------------------
# Venue
# ------------------
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200))

    # Many-to-many with clients
    clients = db.relationship(
        'Client',
        secondary=venue_clients,
        back_populates='venues'
    )

    # One-to-many with events
    events = db.relationship('Event', backref='venue_ref', lazy=True)

# ------------------
# Staff
# ------------------
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50))
    events = db.relationship('Event', secondary='event_staff', backref='staff_members')

# Association table for many-to-many Event <-> Staff
event_staff = db.Table('event_staff',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.id'))
)

# ------------------
# Vehicle
# ------------------
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    license_plate = db.Column(db.String(20))
    events = db.relationship('Event', secondary='event_vehicle', backref='vehicles')

# Association table for many-to-many Event <-> Vehicle
event_vehicle = db.Table('event_vehicle',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicle.id'))
)

# ------------------
# Product
# ------------------
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    events = db.relationship('Event', secondary='event_product', backref='products')

# Association table for many-to-many Event <-> Product
event_product = db.Table('event_product',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

# ------------------
# Event
# ------------------
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    unit_start_time = db.Column(db.Time)
    venue_start_time = db.Column(db.Time)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    extra = db.Column(db.String(200))
    invoice = db.Column(db.String(100))
    notes = db.Column(db.Text)