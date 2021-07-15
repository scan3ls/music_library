from flask import Flask, jsonify
from routes import api
from models.album import Album
import json
from models.db import db

@api.route("/albums", methods=["GET"])
def albums_all():
    try:
        albums = json.loads(str(Album.query.all()))
    except Exception as e:
        db.session.rollback()
        print(e)
        albums = "albums"

    response = jsonify({"Albums": albums})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200

@api.route("/albums/<name>")
def albums_by_name(name):
    albums = Album.query.filter(Album.name == name).first()
    response = jsonify({"Album": album})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
