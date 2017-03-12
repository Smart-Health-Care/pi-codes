from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean



db = SQLAlchemy(app)


class Chamber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    tablets = db.relationship('Tablet', backref='tablets', lazy='dynamic')


Tablet_time = db.Table('Tablet_time',
                       db.Column('tablet_id', db.Integer, db.ForeignKey('tablet.id')),
                       db.Column('time_id', db.Integer, db.ForeignKey('time.id'))
                       )


class Tablet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chamber_id = db.column(db.Integer, db.ForeignKey('chamber.id'))
    name = db.Column(db.String(32), unique=True)
    is_active = db.Column(Boolean)
    prescription = db.Column(db.String(255))
    total_qty_stocked = db.Column(db.Integer)
    total_qty_dispensed = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    stocks = db.relationship('Stock', backref='stocks', lazy='dynamic')
    tablet_taken = db.relationship('Tablet_taken', backref='taken', lazy='dynamic')
    time = db.relationship('Time', secondary=Tablet_time, backref= db.backref('timings',lazy = 'dynamic'))


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty_added = db.Column(db.Integer)
    tablet_id = db.Column(db.Integer, db.ForeignKey('tablet.id'))
    added_at = db.Column(db.DateTime)
    no_of_days = db.Column(db.Integer)


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hrs = db.Column(db.Integer)
    min = db.Column(db.Integer)
    day_of_week = db.Column(db.Integer)


# class Tablet_time(db.Model):
#     tablet_id = db.Column(db.Integer, db.ForeignKey('tablet.id'))
#     time_id = db.Column(db.Integer, db.ForeignKey('time.id'))


class Tablet_taken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tablet_id = db.Column(db.Integer, db.ForeignKey('tablet.id'))
    taken_at = db.Column(db.DateTime)
    is_correct = db.Column(Boolean)
