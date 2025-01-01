from flask import (
    Response, Blueprint, request, redirect, send_file,  url_for,  render_template, 
)
from flask import flash
import os
import logging
from werkzeug.utils import secure_filename
from .db import get_db



bp = Blueprint('api', __name__, url_prefix='/api')
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

messages = []

@bp.route("/")
def hello():
    return "Hello, World!"



@bp.route('/forms', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        first_name = request.form['first-name']
        email = request.form['email']
        message = request.form['message']
        db = get_db()
        error = None
        print(first_name)
        if not first_name:
            flash('Name is required!')
        elif not email:
            flash('Email is required!')
        elif not message:
            flash('Message is required!')            
        if error is None:
            try:
                db.execute(
                    "INSERT INTO forms (first_name, email, message) VALUES (?, ?, ?)",
                    (first_name, email, message),
                )
                db.commit()
            except db.IntegrityError:
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"first_name {first_name} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for('api.create'))
    return '''
    <!doctype html>
<form method=post enctype=multipart/form-data>
    <div>
        <input type="text" id="first-name" placeholder="First Name" name="first-name"autoComplete="first-name" required />
    </div>
    <div>
        <input type="email" id="email" placeholder="Email"name="email" autoComplete="email" required />
    </div>
    <div>
    <textarea id="message" name="message" rows="5" cols="33"></textarea>
    </div>
      <input type=submit value=Upload>
</form>
    '''

@bp.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # type: ignore
            file.save(os.path.join( 'flaskr/static/uploads',filename))
            alpr_file = (os.path.join('flaskr/static/uploads', filename))
            return redirect(url_for('api.upload_file'))
    return '''
    <!doctype html>
    <title>Upload</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''