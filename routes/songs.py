from flask import Flask, jsonify
from routes import api
from models.song import Song
import json
from models.db import db

@api.route("/songs", methods=["GET"])
def songs_all():
    try:
        songs = json.loads(str(Song.query.all()))
    except Exception as e:
        db.session.rollback()
        print(e)
        songs = "songs"

    response = jsonify({"Songs": songs})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200

@api.route("/songs/<song_id>", methods=["GET"])
def song_by_id(song_id):
    song = Song.query.filter(Song.id == song_id).first()

    response = jsonify(json.loads(str(song)))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
