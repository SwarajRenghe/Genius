from flask import Flask
from flask import request, render_template, redirect, request, session, abort, url_for
# from flask.ext.security import SQLAlchemyUserDatastore, Security
import os
from passlib.hash import sha256_crypt
from songs import returnSongs
# from sqLite import addSongToDatabase, printSongList, songClass
from sqLite import *

app = Flask (__name__)


@app.route('/')
def homePage():
    if not session.get('logged_in'):
        return render_template('/login-page')
    else:
        return render_template ('homePage.html')


@app.route('/login-page', methods=['POST','GET'])
def loginPage():
    return render_template('login.html')

@app.route('/login-form-handler', methods=['POST'])
def loginFormHandling():
    login_password = str(request.form['password'])
    hash_password = sha256_crypt.encrypt(login_password) 
    login_username = str(request.form['username'])
    Session = sessionmaker(bind=engine)
    s = Session()
    try:
        query = s.query(User).filter_by(username = login_username).first()
        if var: 
            session['logged_in'] = True
            print "logged in"
            # return redirect(url_for('homePage'))
        else:
            print 'Incorrect username or password entered.'
            # return redirect(url_for('loginPage'))

    except AttributeError:
        print 'Incorrect username or password entered.'
        # return redirect(url_for('loginPage'))


@app.route('/registration-page', methods=['POST','GET'])
def register():
    return render_template('register.html')


@app.route('/registration-form-handler', methods=['POST','GET'])
def registrationFormHandling():
    newUser = User()
    newUser.username = str(request.form['username'])
    pwd = str(request.form['password'])
    newUser.password = sha256_crypt.encrypt(pwd)
    newUser.email = str(request.form['email'])
    newUser.bio = str(request.form['bio'])
    addUserToDatabase(newUser)
    return redirect(url_for('loginPage'))

    
@app.route('/logout-page')
def logout():
    session['logged_in'] = False
    flash('You have succesfully logged out of your account')
    return redirect(url_for('loginPage'))

@app.route('/addSong/')
def addSong():
    return render_template('addSong.html')

@app.route('/my-handling-form-page/')
def songFormHandling():
    if request.method == 'POST':
        user = request.form['songname']
        return user
    else:
        user = request.args.get('songname')
        return user


#
# @app.route('/welcome')
# def welcome():
#   return 'you are on the welcome page'

# @app.route('/user/')
# @app.route('/user/<name>')
# def helloName(name = None):
#   return render_template('users.html', name=name)

@app.route('/songs/')
@app.route('/songs/<int:songNumber>/')
def song(songNumber = None):
    if songNumber is None:
        return render_template('allSongs.html', songs=songs)
    else:
        return render_template('individualSongs.html', songNumber=songNumber, songs=songs)


@app.route('/user/<username>')
# @login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1> Error 404: Page not found </h1>"


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    # app.run(debug=True)
    app.run (debug=True, threaded = True)
