from flask import Flask, jsonify
from routes import api
from models.artist import Artist
import json

@api.route("/artists", methods=["GET"])
def artists_all():
    artists = json.loads(str(Artist.query.all()))
    response = jsonify({"Artists": artists})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
