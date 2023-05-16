from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import db, Vocabulary, Grammar, Image
from sqlalchemy.sql.expression import func
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'db/test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/all_vocabulary', methods=['GET'])
def all_vocabulary():
    vocab_items = Vocabulary.query.all()
    return render_template('all_vocabulary.html', items=vocab_items)


from sqlalchemy.sql.expression import func

@app.route('/vocabulary', methods=['GET', 'POST'])
def vocabulary():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        vocab = Vocabulary(title=title, description=description)
        db.session.add(vocab)
        db.session.commit()
        return redirect(url_for('vocabulary'))

    reminder_item = Vocabulary.query.order_by(func.random()).first()
    return render_template('vocabulary.html', reminder_item=reminder_item)

@app.route('/vocabulary/update/<int:id>', methods=['POST'])
def update_vocabulary(id):
    mastery = request.form.get('mastery')
    vocab = Vocabulary.query.get(id)
    if vocab:
        vocab.mastery = mastery
        db.session.commit()
    return redirect(url_for('vocabulary'))


@app.route('/api/vocabulary', methods=['GET'])
def api_vocabulary():
    vocab_items = Vocabulary.query.all()
    return     jsonify([item.to_dict() for item in vocab_items])

@app.route('/grammar', methods=['GET', 'POST'])
def grammar():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        mastery = request.form.get('mastery')
        gram = Grammar(title=title, description=description, mastery=mastery)
        db.session.add(gram)
        db.session.commit()
        return redirect(url_for('grammar'))

    grammar_items = Grammar.query.all()
    return render_template('grammar.html', items=grammar_items)

@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        image_path = request.form.get('image_path')
        alt_text = request.form.get('alt_text')
        vocabulary_id = request.form.get('vocabulary_id')
        grammar_id = request.form.get('grammar_id')
        image = Image(image_path=image_path, alt_text=alt_text, vocabulary_id=vocabulary_id, grammar_id=grammar_id)
        db.session.add(image)
        db.session.commit()
        return redirect(url_for('image'))

    image_items = Image.query.all()
    return render_template('image.html', items=image_items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


