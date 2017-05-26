from flask import Flask, render_template, url_for, request, redirect, session
from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials
from httplib2 import Http
import json
import sqliteAttempt #import getStudentInfo
import login


app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def about():
    #if session["username"] != None:
     #   pl = "/profile/" + session["username"]
      #  return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = pl)
    #else:
    if login.loggedIn(session):
        return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = login.getEmail())
    else:
        return render_template('home.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), profile_link = None)
        
@app.route("/gallery")
def gallery():
    return render_template('gallery.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), submissions = [
            ["Sebastian Cain", "Spinning Donkey"],
            ["Elias Milborn", "Rotating Mule"],
            ["Nalanda Sharadjaya", "Gyrating Yak"],
            ["Constantine \"I finished my part of the project\" Athanitis", "Revolving Llama"],
            ["Sebastian Cain", "Spinning Donkey"],
            ["Elias Milborn", "Rotating Mule"],
            ["Nalanda Sharadjaya", "Gyrating Yak"],
            ["Constantine \"I finished my part of the project\" Athanitis", "Revolving Llama"],
            ["Sebastian Cain", "Spinning Donkey"],
            ["Elias Milborn", "Rotating Mule"],
            ["Nalanda Sharadjaya", "Gyrating Yak"],
            ["Constantine \"I finished my part of the project\" Athanitis", "Revolving Llama"],
            ["Sebastian Cain", "Spinning Donkey"],
            ["Elias Milborn", "Rotating Mule"],
            ["Nalanda Sharadjaya", "Gyrating Yak"],
            ["Constantine \"I finished my part of the project\" Athanitis", "Revolving Llama"]
            ], profile_link = None)

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
@app.route('/auth', methods = ['POST', 'GET']) # OAuth authentication route
def authenticate():
    flow = flow_from_clientsecrets('client_secrets.json',
                                   scope = 'https://www.googleapis.com/auth/userinfo.email',
                                   redirect_uri = url_for('authenticate', _external = True))

    if 'code' not in request.args: # If we are on the first step of the authentication
        auth_uri = flow.step1_get_authorize_url() # This is the url for the nice google login page
        return redirect(auth_uri) # Redirects to that page
    else: # That login page will redirect to this page but with a code in the request arguments
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code) # This is step two authentication to get the code and store the credentials in a credentials object
        session['credentials'] = credentials.to_json() # Converts the credentials to json and stores it in the session variable
        return redirect(url_for('about'))

if __name__ == '__main__':
    app.rebug = True
    app.run()
