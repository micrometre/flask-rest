from flask import (
    Response, Blueprint, request, redirect, send_file,  url_for,  render_template, 
)
from flask import flash
import os
import logging
from werkzeug.utils import secure_filename



bp = Blueprint('uploads', __name__, url_prefix='/uploads')
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif', 'webp'}
logging.getLogger('flask_cors').level = logging.DEBUG

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('blog.index'))
    return render_template('blog/uploads.html')
    return '''
    <!doctype html>
    <title>Upload</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''