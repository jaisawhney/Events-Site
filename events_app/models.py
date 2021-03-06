"""Create database models to represent tables."""
from events_app import db


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests')


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')


guest_event_table = db.Table('guest_event_table',
                             db.Column('events_id', db.Integer, db.ForeignKey('event.id')),
                             db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
                             )
