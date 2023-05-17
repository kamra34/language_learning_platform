from flask import Flask, render_template
from language_learning_platform.models.models import db, User, Vocabulary, Grammar, Image
from flask_login import LoginManager, current_user, login_required
import os
import secrets
from language_learning_platform.routes.vocabulary import vocabulary
from language_learning_platform.routes.grammar import grammar
from language_learning_platform.routes.image import image
from language_learning_platform.routes.auth import auth

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'db/test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['UPLOAD_FOLDER'] = 'static/uploads/images'  # add this line
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Register the blueprints
app.register_blueprint(vocabulary)
app.register_blueprint(grammar)
app.register_blueprint(image)
app.register_blueprint(auth)

@app.route('/', methods=['GET'])
@login_required
def home():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
