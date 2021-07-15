from flask import Flask, jsonify
from routes import api
from models.album import Album
import json
from models.db import db

@api.route("/", methods=["GET"])
def index():
    try:
        albums = json.loads(str(Album.query.all()))
    except Exception as e:
        db.session.rollback()
        print(e)
        albums = json.loads(str(Album.query.all()))

    response = jsonify({"Albums": albums})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
