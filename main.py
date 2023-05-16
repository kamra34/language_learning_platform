from flask import Flask, render_template
from language_learning_platform.models.models import db, Vocabulary, Grammar, Image
from language_learning_platform.routes.vocabulary import vocabulary
from language_learning_platform.routes.grammar import grammar
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'db/test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db.init_app(app)

# Register the blueprints
app.register_blueprint(vocabulary)
app.register_blueprint(grammar)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)