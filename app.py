from flask import Flask, render_template, url_for, request, redirect, session
import json
import sqliteAttempt #import getStudentInfo


app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def about():
    #if session["username"] != None:
     #   pl = "/profile/" + session["username"]
      #  return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = pl)
    #else:
    return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = None)

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = None)

'''
@app.route('/login/')
def login():
    return render_template('login')

@app.route('/profile/<id>')
def profile(id):
    name = sqliteAttempt.getName(id)
    year = sqliteAttempt.getYear(id))
    return render_template('profile.html', name = name, year = year)
'''

if __name__ == '__main__':
    app.rebug = True
    app.run()
