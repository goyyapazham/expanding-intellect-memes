from flask import Flask, render_template, url_for, request, redirect, session
from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials
from httplib2 import Http
import json
from utils import sqliteUtils, login, imgStrConvert #import getStudentInfo



app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def about():
    #if session["username"] != None:
     #   pl = "/profile/" + session["username"]
      #  return render_template('home.html', students = sqliteUtils.getAllStudents(), assignments = sqliteUtils.displayAllSubmittedAssignments(), profile_link = pl)
    #else:
    print sqliteUtils.getAllGalleries()
    if login.loggedIn(session):
        return render_template('home.html', students = sqliteUtils.getAllStudents(), assignments = sqliteUtils.getAllGalleries(), profile_link = login.getEmail(session).replace('@stuy.edu',''))
    else:
        return render_template('home.html', students = sqliteUtils.getAllStudents(), assignments = sqliteUtils.getAllGalleries(), profile_link = None)
        
@app.route("/gallery/<gID>")
def gallery(gID):
    gID = int(gID)
    print sqliteUtils.getAllSubmissions(gID)
    return render_template('gallery.html', students = sqliteUtils.getAllStudents(), assignments = sqliteUtils.getAllSubmissions(gID), submissions = [], profile_link = None)

'''
@app.route('/login/')
def login():
    return render_template('login') 

@app.route('/profile/<id>')
def profile(id):
    name = sqliteUtils.getName(id)
    year = sqliteUtils.getYear(id))
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
        print "BLAHHHHHHH"
        print session["credentials"]
        if not login.getEmail(session).endswith('@stuy.edu'):
            session.pop('credentials')
            return redirect("/")#add code to say reason for failed login
        return redirect("/")

@app.route('/logout')
def logout():
    session.pop('credentials')
    return redirect("/")

if __name__ == '__main__':
    app.rebug = True
    app.run()
