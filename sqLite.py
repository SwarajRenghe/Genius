from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey

engine = create_engine ("sqlite:///songs.db", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Song (Base):
	__tablename__ = 'songs'
	songnumber = Column (Integer, primary_key = True, autoincrement=True)
	songname = Column (String)
	albumname = Column (String)
	artist = Column (String)
	lyric = Column (String)

def addSongToDatabase (song):
	session = Session()
	Base.metadata.create_all(engine)

	temp = Song()
	temp.songname = song.songname
	temp.albumname = song.albumname
	temp.artist = song.artist
	temp.lyric = song.lyric

	session.add(temp)
	session.commit()
	session.close()


def printSongList ():
	session = Session()
	songs = session.query(Song).all()
	for i in songs:
	    print (str(i.songnumber) + ". " + i.songname + " - " + i.artist)

class songClass:
	songnumber = None;
	songname = None;
	albumname = '';
	artist = '';
	lyric = '';


if __name__ == "__main__":
	for i in range (2):
		s = songClass()
		s.songname = raw_input ("Enter Song Name : ")
		s.albumname = raw_input ("Enter Album Name : ")
		s.artist = raw_input ("Enter Artist Name : ")
		s.lyric = raw_input ("Lyrics : ")
		addSongToDatabase (s);

		printSongList()





# Base.metadata.create_all(engine)


# Adding a couple of songs to the table
# session = Session()

# song1 = Song()
# # song1.songnumber = 1
# song1.songname = "Look What You Made Me Do"
# song1.artist = "Taylor Swift"
# song1.lyric = "Lorem ipsum dolor sit amet"
#
# song2 = Song ()
# # song2.songnumber = 4
# song2.songname = "Say Amen"
# song2.artist = "PANIC! At The Disco"
# song2.lyric = "Lorem ipsum dolor sit amets"
#
#
#
# session.add(song1)
# session.commit()
# session.add(song2)

# songs = session.query(Song).all()
# for i in songs:
#     print i.songnumber
#
# session.commit()
# session.close()
