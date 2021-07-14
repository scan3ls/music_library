from models.db import db
from uuid import uuid4
from models.artist import Artist

class Album(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128))
    artist = db.Column(db.String(128))
    artist_id = db.Column(
        db.String(128),
        db.ForeignKey('artist.id')
    )
    artist_r = db.relationship(
        'Artist',
        backref=db.backref('albums', lazy=True)
    )

    def __init__(self, **kwargs):
        super(Album, self).__init__(**kwargs)

        if self.name is None:
            raise "Album has no name"

        if self.id is None:
            self.id = str(uuid4())

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
        return f'{"*"*100}\n   Album\n\tid={self.id}\n\tname={self.name}\n\tartist={self.artist}\nsongs={self.songs}\n{"*"*100}'
