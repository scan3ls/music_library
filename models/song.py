from models.db import db
from uuid import uuid4
from models.album import Album
from models.artist import Artist

class Song(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    album = db.Column(db.String(128))
    album_id = db.Column(
        db.String(128),
        db.ForeignKey('album.id')
    )
    album_r = db.relationship(
        'Album',
        backref=db.backref('songs', lazy=True)
    )

    artist = db.Column(db.String(128))
    artist_id = db.Column(
        db.String(128),
        db.ForeignKey('artist.id')
    )
    artist_r = db.relationship(
        'Artist',
        backref=db.backref('songs', lazy=True)
    )

    def __init__(self, **kwargs):
        super(Song, self).__init__(**kwargs)

        if self.name is None:
            raise "Song has no name"

        if self.id is None:
            self.id = str(uuid4())

        if self.album:
            query = Album.query.filter(Album.name == self.album).first()
            self.album_id = query.id

        if self.artist:
            query = Artist.query.filter(Artist.name == self.artist).first()
            self.artist_id = query.id


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        import json
        data = {
            "id": self.id,
            "name": self.name,
            "album": self.album,
            "artist": self.artist
        }
        return json.dumps(data, indent=2)
