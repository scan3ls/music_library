from flask import Flask, jsonify
from routes import api
from models.artist import Artist
import json
from models.db import db

@api.route("/artists", methods=["GET"])
def artists_all():
    print("*"*50)
    print(db.session)
    print("*"*50)

    try:
        artists = json.loads(str(Artist.query.all()))
    except Exception as e:
        print(e)
        artists = "artist"

    response = jsonify({"Artists": artists})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
