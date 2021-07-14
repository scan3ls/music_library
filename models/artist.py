from models.db import db
from uuid import uuid4

class Artist(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128))


    def __init__(self, **kwargs):
        super(Artist, self).__init__(**kwargs)

        if self.id is None:
            self.id = str(uuid4())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'{"*"*100}\n  Artist\n\tid={self.id}\n\tname={self.name}\nalbums={self.albums}\n{"*"*100}'
