from flask import Flask, jsonify
from routes import api
from models.artist import Artist
import json
from models.db import db

@api.route("/artists", methods=["GET"])
def artists_all():
    try:
        artists = json.loads(str(Artist.query.all()))
    except Exception as e:
        db.session.rollback()
        print(e)
        artists = "artist"

    response = jsonify({"Artists": artists})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200

@api.route("/artists/<artist_id>")
def albums_by_artist(artist_id):
    try:
        artist = json.loads(str(Artist.query.filter(Artist.id == artist_id).first()))
        albums = artist['albums']
    except Exception as e:
        db.session.rollback()
        print(e)
        albums = 'alubms'

    response = jsonify({"Album": albums})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
