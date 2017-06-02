from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials # OAuth library, import the function and class that this uses
import json # Json library to handle replies
from httplib2 import Http


#given a session, returns whethere the user is logged in
def loggedIn(session):
    #print "AHHHHHHHHHHHHHHH"
    #print "credentials" in session
    #print "BLAHHH"
    #print OAuth2Credentials.from_json(session['credentials']).access_token_expired
    if'credentials' in session:
        if not OAuth2Credentials.from_json(session['credentials']).access_token_expired:
            return True
    return False


#given a session, returns the loggedin user's email
def getEmail(session):
    if loggedIn(session):
        credentials = OAuth2Credentials.from_json(session['credentials'])
        http_auth = credentials.authorize(Http())
        response, content = http_auth.request('https://www.googleapis.com/oauth2/v1/userinfo?alt=json')
        content = json.loads(content)
        return content['email']
    return False
