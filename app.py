from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'{environ.get("DATABASE_URL")}'
db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

@app.route("/")
def index():
    table_names = db.engine.table_names()
    return jsonify({"Tables": table_names}) 

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
