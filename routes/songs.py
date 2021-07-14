from flask import Flask, jsonify
from routes import api
from models.song import Song

@api.route("/songs", methods=["GET"])
def songs_all():
    songs = Song.query.all()
    response = jsonify({"Songs": songs})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
