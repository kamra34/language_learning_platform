# routes/grammar.py
from flask import Blueprint, request, render_template, redirect, url_for
from language_learning_platform.models import Grammar
from language_learning_platform.models.models import db
from sqlalchemy.sql.expression import func
from flask import jsonify

grammar = Blueprint('grammar', __name__, url_prefix='/grammar')

@grammar.route('/', methods=['GET', 'POST'])
def grammar_page():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        gram = Grammar(title=title, description=description)
        db.session.add(gram)
        db.session.commit()
        return redirect(url_for('grammar.grammar_page'))

    reminder_item = Grammar.query.order_by(func.random()).first()
    return render_template('grammar.html', reminder_item=reminder_item)

@grammar.route('/update/<int:id>', methods=['POST'])
def update_grammar(id):
    mastery = request.form.get('mastery')
    gram = Grammar.query.get(id)
    if gram:
        gram.mastery = mastery
        db.session.commit()
    return redirect(url_for('grammar.grammar_page'))

@grammar.route('/all', methods=['GET'])
def all_grammar():
    gramm_items = Grammar.query.all()
    return render_template('all_grammar.html', items=gramm_items)

@grammar.route('/api', methods=['GET'])
def api_grammar():
    gramm_items = Grammar.query.all()
    return jsonify([item.to_dict() for item in gramm_items])
