from flask import Flask, jsonify
from routes import api
from models.album import Album
import json

@api.route("/", methods=["GET"])
def index():
    albums = json.loads(str(Album.query.all()))
    response = jsonify({"Albums": albums})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
