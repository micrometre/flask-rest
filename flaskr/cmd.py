import subprocess
from flask import (
    Response, Blueprint, json, request, redirect, send_file,  url_for,  render_template, 
)
from flask import flash
import os
import logging
from werkzeug.utils import secure_filename
from .db import get_db

from flask_executor import Executor
from flask_shell2http import Shell2HTTP

bp = Blueprint('cmd', __name__, url_prefix='/cmd')
logging.getLogger('flask_cors').level = logging.DEBUG



@bp.route('/', methods=('GET', 'POST'))
def create():
    return render_template('cmd/index.html')