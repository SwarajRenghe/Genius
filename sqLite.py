from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date

engine = create_engine ("sqlite:///executedisshit.db", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User (Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique = True, nullable=False)
    password = Column(String, nullable=False)
    isArtist = Column(Integer, nullable = False)
    bio = Column(String)
    experience = Column(Integer)
    email = Column(String, unique=True, nullable=False)
    annotate = relationship('Annotations',
        backref=backref('ann_users', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    comment = relationship('Comments',
        backref=backref('comm_users', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    singer = relationship('Song',
        backref=backref('art_users', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, username,password,email,isArtist,):

        self.username = username
        self.password = password
        self.email = email
        self.isArtist = isArtist


def addUserToDatabase (user):
    # session = Session()
    # Base.metadata.create_all(engine)

    temp = User(user.username,user.password,user.email,user.isArtist)

    session.add(temp)
    session.commit()
    session.close()


# def printUserList ():
#     session = Session()
#     users = session.query(User).all()
#     for i in users:
#         print (str(i.username) + ". " + i.password + " - " + i.email + "," + i.bio)


class Comments (Base):
    __tablename__ = 'comments'
    c_id = Column(Integer, primary_key = True, autoincrement = True)
    comm_desc = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    song_id = Column(Integer, ForeignKey('songs.songnumber'))


class Annotations (Base):
    __tablename__ = 'annotations'
    ann_id = Column(Integer, primary_key = True, autoincrement = True)
    ann_desc = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    song_id = Column(Integer, ForeignKey('songs.songnumber'))
    range_beg = Column(Integer, nullable = False)
    range_end = Column(Integer, nullable = False)
    upvotes  = Column(Integer)


class Song (Base):
    __tablename__ = 'songs'
    songnumber = Column (Integer, primary_key = True, autoincrement=True)
    songname = Column (String, nullable = False)
    albumname = Column (String)
    artist = Column (String, nullable = False)
    artist_id = Column(Integer, ForeignKey('users.user_id'), nullable= False)
    lyric = Column (String, nullable = False)
    song_annotate = relationship('Annotations',
        backref=backref('ann_songs', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    song_comment = relationship('Comments', #class you're linking to
        backref=backref('comm_songs', lazy='joined'),
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, songname,artist,artist_id,lyric):
        self.songname = songname
        self.artist = artist
        self.artist_id = artist_id
        self.lyric = lyric


def addSongToDatabase (song):
    # session = Session()
    # Base.metadata.create_all(engine)

    temp = Song(song.songname, song.artist, song.artist_id,song.lyric)
    session.add(temp)
    session.commit()
    session.close()

# def updateSongData (song):


def printSongList ():
    # session = Session()
    songs = session.query(Song).all()
    for i in songs:
        print (str(i.songnumber) + ". " + i.songname + " - " + i.artist)


if __name__ == "__main__":
    # for i in range (2):
    #     s = songClass()
    #     s.songname = raw_input ("Enter Song Name : ")
    #     s.albumname = raw_input ("Enter Album Name : ")
    #     s.artist = raw_input ("Enter Artist Name : ")
    #     s.lyric = raw_input ("Lyrics : ")
        # addSongToDatabase (s);

        # printSongList()
    Base.metadata.create_all(engine)
    u1=User("adam","passwod","abc@mail",1)

    addUserToDatabase(u1)

    s = Session()
    try:
        query = s.query(User).filter_by(username = "adam").first()
        print query.username
        print query.user_id
    except:
        pass

    s1=Song("mean","taylor swift",query.user_id,"none available")
    addSongToDatabase(s1)
    try:
        query = s.query(Song).filter_by(songname = "mean").first()
        print query.artist_id
        print query.art_users.username
    except:
        pass
