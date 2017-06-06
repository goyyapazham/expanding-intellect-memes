from flask import Flask, render_template, url_for, request, redirect, session
from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials
from httplib2 import Http
import json
import time
from utils import sqliteUtils, login, imgStrConvert #import getStudentInfo
from PIL import Image
import datetime


app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
@app.route('/<message>')
def about(message=""):
    #if session["username"] != None:
     #   pl = "/profile/" + session["username"]
      #  return render_template('home.html', students = sqliteUtils.getAllStudents(), assignments = sqliteUtils.displayAllSubmittedAssignments(), profile_link = pl)
    #else:
    print sqliteUtils.getAllGalleries()
    if login.isAdmin(session):
        return render_template('home.html', galleries = sqliteUtils.getAllGalleries(), profile_link = login.getEmail(session).replace('@stuy.edu',''), admin = True)
    elif login.loggedIn(session):
        return render_template('home.html', galleries = sqliteUtils.getAllGalleries(), profile_link = login.getEmail(session).replace('@stuy.edu',''), admin = False)
    else:
        return render_template('home.html', galleries = sqliteUtils.getAllGalleries(), profile_link = None, message = message, admin = False)



    
'''        
@app.route("/gallery")
def gallery():
    return render_template('gallery.html', students = sqliteAttempt.displayStudentInfo(), assignments = sqliteAttempt.displayAllSubmittedAssignments(), submissions = [], profile_link = None, image=None)
'''
@app.route("/gallery/<gID>")
@app.route("/gallery/<gID>/<message>")
def gallery(gID,message=""):
    gID = int(gID)
    print sqliteUtils.getAllSubmissions(gID)
    if login.isAdmin(session):
        return render_template('gallery.html', galleries = sqliteUtils.getAllGalleries(), submissions = sqliteUtils.getAllSubmissions(gID), profile_link = login.getEmail(session).replace('@stuy.edu',''), gID = gID, message=message, admin = True)
    elif login.loggedIn(session):
         return render_template('gallery.html', galleries = sqliteUtils.getAllGalleries(), submissions = sqliteUtils.getAllSubmissions(gID), profile_link = login.getEmail(session).replace('@stuy.edu',''), gID = gID, message=message, admin = False)
    else:
        return render_template('gallery.html', galleries = sqliteUtils.getAllGalleries(), submissions = sqliteUtils.getAllSubmissions(gID), profile_link = None, gID = gID, message=message, admin = False)




    
    
@app.route("/upload/<gID>", methods = ['POST', 'GET'])
def upload(gID):
    if not login.loggedIn(session):
        return redirect(url_for("gallery", gID = str(gID), message = "must be logged in"))
    gID = int(gID)
    title = request.form['filename']
    script = ""
    if 'script' in request.form:
        script = request.form['script']
    img = request.files['file']
    imgName = img.filename
    ext = imgName.split(".")[-1]
    ext = ext.lower()
    baseName = str(int(time.time()*1000))
    newName = baseName + "." + ext
    if ext != "gif" and ext != "png" and ext != "ppm":
        return redirect(url_for("gallery", gID = str(gID), message = "filetype must be ppm, png, or gif"))   
    img.save("static/Images/" + newName)
    icon = Image.open("static/Images/" + newName)
    iconSize = (250, 250)
    icon.thumbnail(iconSize)
    iconName = baseName + ".png"
    icon.save("static/Icons/" + iconName)
    sqliteUtils.addSubmission(gID, title, login.getEmail(session).replace("@stuy.edu",""), "Images/" + newName, "Icons/" + iconName, script, str(datetime.datetime.now()))
    return redirect(url_for("gallery", gID = str(gID)))




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
        if not login.getEmail(session).endswith('@stuy.edu') and not login.isAdmin(session):
            session.pop('credentials')
            return redirect(url_for("about", message="stuy.edu emails only - "))#add code to say reason for failed login
        return redirect("/")

@app.route('/logout')
def logout():
    session.pop('credentials')
    return redirect("/")

if __name__ == '__main__':
    app.rebug = True
    app.run()
