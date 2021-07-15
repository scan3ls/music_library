from flask import Flask, jsonify
from routes import api
from models.song import Song
import json

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
