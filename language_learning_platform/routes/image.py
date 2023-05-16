# routes/image.py
from flask import Blueprint, render_template, request, redirect, url_for
from language_learning_platform.models.models import db, Image
from sqlalchemy.sql.expression import func
from flask import jsonify

image = Blueprint('image', __name__, url_prefix='/image')

@image.route('/', methods=['GET', 'POST'])
def image_page():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_path = request.form.get('image_path')
        img = Image(title=title, description=description, image_path=image_path)
        db.session.add(img)
        db.session.commit()
        return redirect(url_for('image.image_page'))

    reminder_item = Image.query.order_by(func.random()).first()
    return render_template('image.html', reminder_item=reminder_item)

@image.route('/all_image', methods=['GET'])
def all_image():
    image_items = Image.query.all()
    return render_template('all_image.html', items=image_items)

@image.route('/image/update/<int:id>', methods=['POST'])
def update_image(id):
    mastery = request.form.get('mastery')
    img = Image.query.get(id)
    if img:
        img.mastery = mastery
        db.session.commit()
    return redirect(url_for('image.image_page'))

@image.route('/api/image', methods=['GET'])
def api_image():
    image_items = Image.query.all()
    return jsonify([item.to_dict() for item in image_items])
