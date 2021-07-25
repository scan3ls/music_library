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

@api.route("/albums/<album_id>")
def albums_by_id(album_id):
    try:
        album = json.loads(str(Album.query.filter(Album.id == album_id).first()))
    except Exception as e:
        db.session.rollback()
        print(e)
        album = "album"

    response = jsonify(album)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
