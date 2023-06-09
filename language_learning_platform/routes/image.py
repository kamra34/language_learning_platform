# routes/image.py
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required
from language_learning_platform.models.models import db, Image
from sqlalchemy.sql.expression import func
from werkzeug.utils import secure_filename
from flask import jsonify
import os
import json

image = Blueprint('image', __name__, url_prefix='/image')

UPLOAD_FOLDER = 'uploads/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@image.route('/', methods=['GET', 'POST'])
@login_required
def image_page():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_file = request.files['image']
        filename = secure_filename(image_file.filename)  # use secure_filename to ensure a safe filename
        if allowed_file(filename):
            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path)
            img = Image(title=title, description=description, image_filename=filename)  # pass the filename, not the path
            db.session.add(img)
            db.session.commit()
        return redirect(url_for('image.image_page'))
    reminder_item = Image.query.order_by(func.random()).first()
    if reminder_item:
        file_type = 'pdf' if reminder_item.image_filename.rsplit('.', 1)[1].lower() == 'pdf' else 'image'
    else:
        file_type = 'image'
    # Get all Image items
    image_items = Image.query.all()

    # Convert the items to a list of dictionaries
    image_items = [item.to_dict() for item in image_items]

    # Convert the list to JSON
    image_items_json = json.dumps(image_items)

    return render_template('image.html', reminder_item=reminder_item, image_items_json=image_items_json, file_type=file_type)

@image.route('/all_image', methods=['GET'])
def all_image():
    image_items = Image.query.all()
    return render_template('all_image.html', items=image_items)

@image.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_image(id):
    img = Image.query.get(id)
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_file = request.files.get('image')  # Here we get the new image from the form
        if image_file:
            filename = secure_filename(image_file.filename)
            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path)
            img.image_filename = filename  # If a new image was uploaded, we update the filename in the database
        if title:
            img.title = title
        if description:
            img.description = description
        db.session.commit()
        return redirect(url_for('image.all_image'))
    return render_template('update_image.html', image=img)

@image.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_image(id):
    img = Image.query.get(id)
    if img:
        db.session.delete(img)
        db.session.commit()
    return redirect(url_for('image.all_image'))

@image.route('/api/image', methods=['GET'])
@login_required
def api_image():
    image_items = Image.query.all()
    return jsonify([item.to_dict() for item in image_items])
