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
        ping_google = request.form['ping-google']
        alpr_arg1 = "-c"
        alpr_arg2 = "3"
        alpr_arg3 = "google.com"
        output = subprocess.check_output(['ping', str(alpr_arg1), alpr_arg2, alpr_arg3 ]).decode('utf-8')
        if not ping_google:
          flash('Last is required!')
        else:
            messages.append({
                'ping-google': output
                    })
            print(messages)
            return redirect(url_for('api.create'))
    return render_template('proc/index.html', messages=messages)