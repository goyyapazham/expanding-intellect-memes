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
    print q
    c.execute(q)


def submitToStudents(name, password, year):
    insert = "INSERT INTO studentInfo VALUES ('%s','%s',%d,NULL);"%(name, password, year)
    #print insert
    c.execute(insert)


def deleteFromStudents(id):
    delete = "DELETE FROM studentInfo WHERE id = %d;"%(id)
    #print delete
    c.execute(delete)


def displayStudentInfo():
    display = "SELECT * FROM studentInfo"
    #print display
    c.execute(display)
    print c.fetchall()
    
#createStudents()    
#submitToStudents("Costa", "pass1", 2017)
#submitToStudents("Nala", "pass2", 2016)
#submitToStudents("Elias", "pass3", 2017)
#submitToStudents("Sebastian","pass4",2018)
#displayStudentInfo()
#deleteFromStudents(3)
displayStudentInfo()
print
print
print
print





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
    q = "CREATE TABLE assignments (aNum INTEGER, title TEXT, studentID INTEGER, imageText TEXT, upvotes INTEGER, script TEXT)"
    print q
    c.execute(q)

    
def addWork(aNum, title, studentID, imageText, upvotes, script):
    insert = "INSERT INTO assignments VALUES (%d,'%s',%d,'%s',%d,'%s');"%(aNum,title,studentID,imageText,upvotes,script)
    #print insert
    c.execute(insert)

def displayAllSubmittedAssignments():
    display = "SELECT * FROM assignments"
    #print display
    c.execute(display)
    print c.fetchall()

def addUpvotes(studentID, aNum, upvoteNum):
    getNum = "SELECT upvotes FROM assignments WHERE studentID = %d AND aNum = %d"%(studentID,aNum)
    curr = c.execute(getNum)
    newUpvote = curr + upvoteNum
    add = "UPDATE assignments SET upvotes = %d WHERE studentID = %d AND aNum = %d"%(newUpvote,studentID,aNum)
    c.execute(add)


#createAssignment()
#addWork(1, "Assignment 1", 2,"this is the ascii text of the image", 0, "this is the script text for the work")
#addWork(3, "Assignment 3", 2,"OTHER this is the ascii text of the image", 3, "OTHERthis is the script text for the work")
displayAllSubmittedAssignments()
addUpvotes(2,1,5)
displayAllSubmittedAssignments()

    
db.commit()
db.close()
