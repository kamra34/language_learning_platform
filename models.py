from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')
    images = db.relationship('Image', backref='vocabulary', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'mastery': self.mastery,
            'images': [image.to_dict() for image in self.images]
        }


class Grammar(db.Model):
    __tablename__ = 'grammar'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    mastery = db.Column(db.String(20), nullable=False, default='Show More')
    images = db.relationship('Image', backref='grammar', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'mastery': self.mastery,
            'images': [image.to_dict() for image in self.images]
        }

class Image(db.Model):
    __tablename__ = 'images'

    image_id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String, nullable=False)
    alt_text = db.Column(db.String, nullable=False)
    vocabulary_id = db.Column(db.Integer, db.ForeignKey('vocabulary.id'), nullable=True)
    grammar_id = db.Column(db.Integer, db.ForeignKey('grammar.id'), nullable=True)

    def to_dict(self):
        return {
            'image_id': self.image_id,
            'image_path': self.image_path,
            'alt_text': self.alt_text,
            'vocabulary_id': self.vocabulary_id,
            'grammar_id': self.grammar_id
        }
