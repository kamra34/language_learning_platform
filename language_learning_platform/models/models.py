from flask_sqlalchemy import SQLAlchemy
import os
from flask import current_app

db = SQLAlchemy()

class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'mastery': self.mastery
        }


class Grammar(db.Model):
    __tablename__ = 'grammar'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'mastery': self.mastery
        }

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    image_filename = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')

    def __init__(self, title, image_filename, description, mastery='Show More'):
        self.title = title
        self.image_filename = image_filename
        self.description = description
        self.mastery = mastery

    @property
    def image_path(self):
        return os.path.join('uploads', 'images', self.image_filename).replace('\\', '/')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image_filename': self.image_filename,
            'image_path': self.image_path,  # call the property here
            'description': self.description,
            'mastery': self.mastery
        }

