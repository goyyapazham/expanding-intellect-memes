import sqlite3

fileName = "sqliteDB.db"

db = sqlite3.connect(fileName)
c = db.cursor()

"""
MongoDB CONVERSIONS:

COLLECTION -> TABLE
DOCUMENT PROPERTY -> COLUMN/CELL IN TABLE

"""

###StudentInfo Table
###discrepancy: in our code, the student id is the id we create for the student
###in reality, we can ask mr. dw to input their osis number.

def createStudents():
    
    q = "CREATE TABLE studentInfo (name TEXT, password TEXT, year INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT)"
   # print q
    c.execute(q)


def submitToStudents(name, password, year):
    insert = "INSERT INTO studentInfo VALUES ('%s','%s',%d,NULL);"%(name, password, year)
    #print insert
    c.execute(insert)
    db.commit()


def deleteFromStudents(id):
    delete = "DELETE FROM studentInfo WHERE id = %d;"%(id)
    #print delete
    c.execute(delete)
    db.commit()


def displayStudentInfo():
    display = "SELECT * FROM studentInfo"
    #print display
    c.execute(display)
    return c.fetchall()

#GET FUNCTIONS....given ID, get various info from student table

def getName(iD):
    get = "SELECT name FROM studentInfo WHERE id = %d"%(iD)
    display = c.execute(get).fetchone()[0]
    #print display
    return display

def getYear(iD):
    get = "SELECT year FROM studentInfo WHERE id = %d"%(iD)
    display = c.execute(get).fetchone()[0]
    return display

 
    
#createStudents()    
#submitToStudents("Costa", "pass1", 2017)
#submitToStudents("Nala", "pass2", 2016)
#submitToStudents("Elias", "pass3", 2017)
#submitToStudents("Sebastian","pass4",2018)
#displayStudentInfo()
#deleteFromStudents(3)

'''
displayStudentInfo()
print
print
print
print

'''



###ASSIGNMENTS TABLES
###have to test out if i can use variable table name...to create a
###single table per assignment

'''*************************************************************
test later to see if below code works

import sqlite3
conn = sqlite3.connect('db.db')
c = conn.cursor()
tablename, field_data = 'some_table','some_data'
query = 'SELECT * FROM '+tablename+' WHERE column1=\"'+field_data+"\""
c.execute(query)
'''



###as of right now, im just creating one table with ALL assignments

def createAssignment():
    q = "CREATE TABLE assignments (assignmentNumber INTEGER, title TEXT, studentID INTEGER, imageText TEXT, upvotes INTEGER, script TEXT)"
   # print q
    c.execute(q)


#USE imgStrConvert to get the image text    
def addWork(aNum, title, studentID, imageText, upvotes, script):
    insert = "INSERT INTO assignments VALUES (%d,'%s',%d,'%s',%d,'%s');"%(aNum,title,studentID,imageText,upvotes,script)
    #print insert
    c.execute(insert)
    db.commit()

def displayAllSubmittedAssignments():
    display = "SELECT * FROM assignments"
    #print display
    c.execute(display)
    return c.fetchall()

def addUpvotes(studentID, aNum, upvoteNum):
    getNum = "SELECT upvotes FROM assignments WHERE studentID = %d AND assignmentNumber = %d"%(studentID,aNum)
    curr = c.execute(getNum).fetchone()
   # print curr
   # print curr[0]
    newUpvote = curr[0] + upvoteNum
    add = "UPDATE assignments SET upvotes = %d WHERE studentID = %d AND assignmentNumber = %d"%(newUpvote,studentID,aNum)
    c.execute(add)
    db.commit()

#GET FUNCTIONS....input is studentID and assignment number. returns the rest of the info

def getName(sID):
    get = "SELECT name FROM studentInfo WHERE id == %d"%(sID)
    display = c.execute(get).fetchone()[0]
    return display

def getYear(sID):
    get = "SELECT year FROM studentInfo WHERE id == %d"%(sID)
    display = c.execute(get).fetchone()[0]
    return display

#def get<INFO TO RETURN> (studentID, assignmentNumber)

def getTitle(sID, aNum):
    get = "SELECT title FROM assignments WHERE studentID = %d AND assignmentNumber = %d"%(sID,aNum)
    display = c.execute(get).fetchone()[0]
    return display


#Use imgStrConvert to convert the returned string to image
def getImageText(sID, aNum):
    get = "SELECT imageText FROM assignments WHERE studentID = %d AND assignmentNumber = %d"%(sID,aNum)
    display = c.execute(get).fetchone()[0]
    return display

def getUpvotes(sID, aNum):
    get = "SELECT upvotes FROM assignments WHERE studentID = %d AND assignmentNumber = %d"%(sID,aNum)
    display = c.execute(get).fetchone()[0]
    return display

def getScript(sID, aNum):
    get = "SELECT script FROM assignments WHERE studentID = %d AND assignmentNumber = %d"%(sID,aNum)
    display = c.execute(get).fetchone()[0]
    return display



#createAssignment()
#addWork(1, "Assignment 1", 2,"this is the ascii text of the image", 0, "this is the script text for the work")
#addWork(3, "Assignment 3", 2,"OTHER this is the ascii text of the image", 3, "OTHERthis is the script text for the work")
#displayAllSubmittedAssignments()
#addUpvotes(2,3,5)
#displayAllSubmittedAssignments()

    
#db.commit()
#db.close()

########################################################################
#Creating the Gallery Table

def createGallery():
    q = "CREATE TABLE galleries (title TEXT, galleryNum INTEGER PRIMARY KEY AUTOINCREMENT)"
   # print q
    c.execute(q)

def getAllSubmissionsFromGallery(galleryNum):
    display = "SELECT * FROM assignments WHERE assignmentNumber = %d"%(galleryNum)
    #print display
    c.execute(display)
    return c.fetchall()

print getAllSubmissionsFromGallery(1)

def addGallery(galleryTitle):
    insert = "INSERT INTO galleries VALUES('%s', NULL)"%(galleryTitle)
    print "added to gallery table"
    c.execute(insert)
    db.commit()


def getTitle(galleryNum):
    display = "SELECT title FROM galleries WHERE galleryNum = %d"%(galleryNum)
    c.execute(display)
    return c.fetchall()

def getAllGalleries():
    display = "SELECT * FROM galleries"
    c.execute(display)
    return c.fetchall()

def delGallery(galleryTitle):
    delete = "DELETE FROM galleries WHERE title = '%s'"%(galleryTitle)
    c.execute(delete)
    db.commit()

#createGallery()
#addGallery("Gallery 1")
#addGallery("gallery 2")
#addGallery("gallery 3")
#print getAllSubmissionsFromGallery(1)

#print getAllGalleries()
#delGallery("gallery 2")
#print getAllGalleries()
