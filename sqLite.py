from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey

engine = create_engine ("sqlite:///songs.db", echo=True)

Base = declarative_base()

class Song (Base):
	__tablename__ = 'songs'
	songnumber = Column ('songnumber', Integer, primary_key = True)
	songname = Column ('songname', String)
	artist = Column ('artist', String)
	lyric = Column ('lyric', String)

Base.metadata.create_all(engine)


# Adding a couple of songs to the table
Session = sessionmaker(bind=engine)
session = Session()

song1 = Song()
song1.songnumber = 1;
song1.songname = "Look What You Made Me Do"
song1.artist = "Taylor Swift"
song1.lyric = "Lorem ipsum dolor sit amet"

song2 = Song ()
song2.songnumber = 2;
song2.songname = "Say Amen"
song2.artist = "PANIC! At The Disco"
song2.lyric = "Lorem ipsum dolor sit amets"

session.add(song1)
session.add(song2)

# songs = session.query(Song).all()
# for i in songs:
#     print i.artist

session.commit()
session.close()
