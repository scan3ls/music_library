from models.db import db
from uuid import uuid4
from models.album import Album

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


    def __init__(self, **kwargs):
        super(Song, self).__init__(**kwargs)

        if self.name is None:
            raise "Song has no name"

        if self.id is None:
            self.id = str(uuid4())

        if self.album:
            query = Album.query.filter(Album.name == self.album).first()
            self.album_id = query.id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'{"*"*100}\n    Song\n\tid={self.id}\n\tname={self.name}\n\talbum={self.album}\n{"*"*100}'
