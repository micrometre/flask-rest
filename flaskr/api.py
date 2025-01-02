import subprocess
from flask import (
    Response, Blueprint, json, request, redirect, send_file,  url_for,  render_template, 
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






@bp.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        print(first_name)
        if not first_name:
            flash('Name is required!')
        elif not last_name:
            flash('Last is required!')
        else:
            messages.append({
                'first-name': first_name,
                  'last-name': last_name,
                    })
   
            return redirect(url_for('api.create'))
    return render_template('proc/index.html', messages=messages)