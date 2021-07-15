from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from models import *
from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'{environ.get("DATABASE_URL")}'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
CORS(app, resources={r"*": {"origins": "*"}})
db.init_app(app)
app.app_context().push()

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
