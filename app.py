from flask import Flask, render_template, url_for, request, redirect, session
import json
import sqliteAttempt #import getStudentInfo

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def about():
    return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.getAllSubmittedAssignments())

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
