import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "app"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()


'''
Cars

'''


class Cars(db.Model):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    color = Column(String)
    driver_id = Column(Integer, ForeignKey('driver.id'))

    def __init__(self, model, color, driver_id):
        self.color = color
        self.model = model
        self.driver_id = driver_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'model': self.model,
            'color': self.color,
            'driver_id': self.driver_id
        }


'''
Driver

'''


class Driver(db.Model):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }
