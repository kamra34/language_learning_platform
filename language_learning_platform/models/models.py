from flask_sqlalchemy import SQLAlchemy

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
    image_path = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image_path': self.image_path,
            'description': self.description,
            'mastery': self.mastery
        }
