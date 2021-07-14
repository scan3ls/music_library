from flask import Flask, jsonify
from routes import api
from models.artist import Artist

@api.route("/artists", methods=["GET"])
def artists_all():
    artists = Artist.query.all()
    response = jsonify({"Artists": artists})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
