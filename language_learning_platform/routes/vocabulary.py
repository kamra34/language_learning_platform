from flask import Blueprint, request, render_template, redirect, url_for
#from language_learning_platform.models import Vocabulary
from language_learning_platform.models.models import db, Vocabulary
from sqlalchemy.sql.expression import func
from flask import jsonify

vocabulary = Blueprint('vocabulary', __name__, url_prefix='/vocabulary')

@vocabulary.route('/', methods=['GET', 'POST'])
def vocabulary_page():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        vocab = Vocabulary(title=title, description=description)
        db.session.add(vocab)
        db.session.commit()
        return redirect(url_for('vocabulary.vocabulary_page'))

    reminder_item = Vocabulary.query.order_by(func.random()).first()
    return render_template('vocabulary.html', reminder_item=reminder_item)

@vocabulary.route('/update/<int:id>', methods=['POST'])
def update_vocabulary(id):
    title = request.form.get('title')
    description = request.form.get('description')
    vocab = Vocabulary.query.get(id)
    if vocab:
        vocab.title = title
        vocab.description = description
        db.session.commit()
    return redirect(url_for('vocabulary.all_vocabulary'))

@vocabulary.route('/delete/<int:id>', methods=['POST'])
def delete_vocabulary(id):
    vocab = Vocabulary.query.get(id)
    if vocab:
        db.session.delete(vocab)
        db.session.commit()
    return redirect(url_for('vocabulary.all_vocabulary'))

@vocabulary.route('/all', methods=['GET'])
def all_vocabulary():
    vocab_items = Vocabulary.query.all()
    return render_template('all_vocabulary.html', items=vocab_items)

@vocabulary.route('/api', methods=['GET'])
def api_vocabulary():
    vocab_items = Vocabulary.query.all()
    return jsonify([item.to_dict() for item in vocab_items])


