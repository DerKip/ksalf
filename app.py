from flask import Flask, render_template, request , redirect, url_for, \
flash , session
from functools import wraps
import sqlite3

app=Flask(__name__) #setting up our WSGI app from flask

app.secret_key='siri'
app.database="sample.db"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap (*args ,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first .')
            return redirect(url_for('login'))
    return wrap
# use decorator to link function to url

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid creadentials, please try again'
        else:
            session['logged_in']=True
            flash('logged in')
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('logged out')
    return redirect(url_for('welcome'))


if __name__=='__main__':
    app.run(debug=True)
