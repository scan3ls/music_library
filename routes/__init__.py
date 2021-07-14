from flask import Blueprint

api = Blueprint('api', __name__, url_prefix="")

from routes.index import *
from routes.songs import *
from routes.albums import *
from routes.artist import *
