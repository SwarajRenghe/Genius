from flask_sqlalchemy import SQLAlchemy, event
from sqlalchemy import engine

db = SQLAlchemy()

# noinspection PyUnusedLocal
@event.listens_for(engine.Engine, 'connect')
def __set_sqlite_pragma(db_conn, conn_record):
    cursor = db_conn.cursor()
    cursor.execute('PRAGMA foreign_keys=ON;')
cursor.close()


class User(db.Model):
    # Default __tablename__ = customer
    __tablename__ = 'user-table'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer)
    email = db.Column(db.String(10), unique=True, nullable=False)
    music_contrib = db.relationship(
        'Contributions',
        backref=db.backref('user-table', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
           	'password': self.password,
           	'experience': self.experience,
           	'email': self.email
        }

    def __repr__(self):
		return self.serialize().__repr__()


class Track(db.Model):
    # Default __tablename__ = customer
    __tablename__ = 'songs-table'

    track_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_name = db.Column(db.String(100), nullable=False)
    album_name = db.Column(db.String(100))
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    track_lyrics = db.Column(db.String(4000))
    lyric_id = db.relationship(
        'Lyrics',
        backref=db.backref('songs-table', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def serialize(self):
        return {
            'id': self.id,
            'track_name': self.track_name,
           	'artist': self.artist,
           	'genre': self.genre,
        }

    def __repr__(self):
return self.serialize().__repr__()

"""create an identifying relationship"""

class Lyrics(db.Model):
    # Default __tablename__ = customer
    __tablename__ = 'lyrics-table'

    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lyrics_line1 = db.Column(db.String(200))