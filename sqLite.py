from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date

engine = create_engine ("sqlite:///songs.db", echo=True)
engine = create_engine ("sqlite:///users.db", echo=True)


Base = declarative_base()
Session = sessionmaker(bind=engine)

class User (Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique = True, nullable=False)
    password = Column(String, nullable=False)
    bio = Column(String)
    experience = Column(Integer)
    email = Column(String, unique=True, nullable=False)
    # music_contrib = relationship(
    #     'Contributions',
    #     backref=backref('users', lazy='joined'),
    #     cascade="all, delete-orphan",
    #     passive_deletes=True
    # )

    def __init__(self, username, password, email):
    
        self.username = username
        self.password = password
        self.email = email

def addUserToDatabase (user):
    session = Session()
    Base.metadata.create_all(engine)

    temp = User()
    temp.username = user.username
    temp.password  = user.password
    temp.bio = user.bio
    temp.experience = 0
    temp.email = user.email

    session.add(temp)
    session.commit()
    session.close()


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

# def updateSongData (song):


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