from flask import Flask
from flask import request, render_template
from songs import returnSongs
from sqLite import addSongToDatabase, printSongList, songClass
# from sqLite import *

app = Flask (__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./songs.db'

# from sqlalchemy.orm import sessionmaker, relationship, backref
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey


# user_agent = request.headers.get('User-Agent')
# return '<p>Your browser is %s</p>' % user_agent

# songs = returnSongs();

@app.route('/')
def homePage():
	return render_template ('homePage.html')

@app.route('/addSong')
def addSong():
	return render_template('addSong.html')

@app.route('/my-handling-form-page')
def formHandling():
	if request.method == 'POST':
		user = request.form['songname']
		return user
	else:
		user = request.args.get('songname')
		return user

#
# @app.route('/welcome')
# def welcome():
# 	return 'you are on the welcome page'

# @app.route('/user/')
# @app.route('/user/<name>')
# def helloName(name = None):
# 	return render_template('users.html', name=name)

@app.route('/songs')
@app.route('/songs/<int:songNumber>')
def song(songNumber = None):
	if songNumber is None:
		return render_template('allSongs.html', songs=songs)
	else:
		return render_template('individualSongs.html', songNumber=songNumber, songs=songs)

# @app.route('')

@app.errorhandler(404)
def page_not_found(e):
	return "<h1> Error 404: Page not found </h1>"
#
#
# engine = create_engine ("sqlite:///songs.db", echo=True)
#
# Base = declarative_base()
#
# class Song (Base):
# 	__tablename__ = 'songs'
# 	songnumber = Column ('songnumber', Integer, primary_key = True)
# 	songname = Column ('songname', String)
# 	artist = Column ('artist', String)
# 	lyric = Column ('lyric', String)
#
#
# song1 = Song()
# # Song().storage.drop()
# song1.songnumber = 0;
# song1.songname = "Look What You Made Me Do"
# song1.artist = "Taylor Swift"
# song1.lyric = "Lorem ipsum dolor sit amet"
# #
#
# Base.metadata.create_all(engine)
#
#
# # Adding a couple of songs to the table
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # song2 = Song ()
# # song2.songNumber = 2;
# # song2.songname = "Say Amen"
# # song2.artist = "PANIC! At The Disco"
# # song2.lyric = "Lorem ipsum dolor sit amets"
#
# session.add(song1)
# # session.add(song2)
#
# session.commit()
# session.close()
#
#
#
#

if __name__ == "__main__":
	app.run (debug=True)
