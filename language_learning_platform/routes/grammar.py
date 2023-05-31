# routes/grammar.py
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from language_learning_platform.models.models import db, Grammar
from sqlalchemy.sql.expression import func
from flask import jsonify
import json

grammar = Blueprint('grammar', __name__, url_prefix='/grammar')

@grammar.route('/', methods=['GET', 'POST'])
@login_required
def grammar_page():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        gram = Grammar(title=title, description=description)
        db.session.add(gram)
        db.session.commit()
        return redirect(url_for('grammar.grammar_page'))

    reminder_item = Grammar.query.order_by(func.random()).first()
    # Get all Grammar items
    grammar_items = Grammar.query.all()

    # Convert the items to a list of dictionaries
    grammar_items = [
        {
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'mastery': item.mastery
        }
        for item in grammar_items
    ]

    # Convert the list to JSON
    grammar_items_json = json.dumps(grammar_items)

    return render_template('grammar.html', reminder_item=reminder_item, grammar_items_json=grammar_items_json)

@grammar.route('/update/<int:id>', methods=['POST'])
@login_required
def update_grammar(id):
    title = request.form.get('title')
    description = request.form.get('description').replace('\r\n', '\n')
    gramm = Grammar.query.get(id)
    if gramm:
        gramm.title = title
        gramm.description = description
        db.session.commit()
    return redirect(url_for('grammar.all_grammar'))

@grammar.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_grammar(id):
    gramm = Grammar.query.get(id)
    if gramm:
        db.session.delete(gramm)
        db.session.commit()
    return redirect(url_for('grammar.all_grammar'))

@grammar.route('/all', methods=['GET'])
@login_required
def all_grammar():
    gramm_items = Grammar.query.all()
    return render_template('all_grammar.html', items=gramm_items)

@grammar.route('/api', methods=['GET'])
def api_grammar():
    gramm_items = Grammar.query.all()
    return jsonify([item.to_dict() for item in gramm_items])
