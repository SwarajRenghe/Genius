from flask import Flask
from flask import request, render_template
from songs import returnSongs
from sqLite import addSongToDatabase, printSongList, songClass
# from sqLite import *

app = Flask (__name__)

@app.route('/login-page')
def loginPage():
    render_template('login.html')

if __name__ == "__main__":
    app.run (debug=True)