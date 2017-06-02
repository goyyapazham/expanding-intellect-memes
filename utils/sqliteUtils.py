import sqlite3

filename = "data.db"

db = sqlite3.connect(filename)
c = db.cursor()

## STUDENTS TABLE

#create students table (only use once!)
def createStudents():
    c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, password TEXT, year INTEGER, id TEXT)")

#add student to table
def addStudent(name, password, year, sID):
    q = "INSERT INTO students VALUES ('%s','%s',%d,'%s')"%(name, password, year, sID)
    c.execute(q)
    db.commit()

#remove student from table
def deleteStudent(sID):
    q = "DELETE FROM students WHERE id = '%s'"%(sID)
    c.execute(q)
    db.commit()

#get name of student w sID
def getName(sID):
    q = "SELECT name FROM students WHERE id = '%s'"%(sID)
    return c.execute(q).fetchone()[0]

#get yr of student w sID
def getYear(sID):
    q = "SELECT year FROM students WHERE id = '%s'"%(sID)
    return c.execute(q).fetchone()[0]


## GALLERIES/ASSIGNMENTS

#create galleries table (only use once!)
def createGalleries():
    c.execute("CREATE TABLE IF NOT EXISTS galleries (title TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)")

#create submissions table (only use once!)
def createSubmissions():
    c.execute("CREATE TABLE IF NOT EXISTS submissions (galleryID INTEGER, title TEXT, sID TEXT, imageData TEXT, miniImageData TEXT, script TEXT, time TEXT)")

#add assignment (to galleries table)
def addAssignment(title):
    q = "INSERT INTO galleries VALUES ('%s', NULL)"%(title)
    c.execute(q)
    db.commit()

#get assignment ID (assumes gallery title is unique)
def getAssignmentID(title):
    q = "SELECT id FROM galleries WHERE title = '%s'"%(title)
    return c.execute(q).fetchone()[0]

#add submission (to submissions table)
def addSubmission(gID, title, sID, img, mini, script, time):
    q = "INSERT INTO submissions VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s')"%(gID, title, sID, img, mini, script, time)
    c.execute(q)
    db.commit()

## RETURN DICTIONARIES

#get all galleries
#assignments = galleries
#changed the naming for easier understanding
def getAllGalleries():
    assignments = []
    for assignment in c.execute("SELECT * FROM galleries").fetchall():
        assignments += [ {"galleryName": str(assignment[0]), "gID": assignment[1]} ]
    return assignments
    
#get all submissions for a given gallery
def getAllSubmissions(gID):
    subs = []
    for sub in c.execute("SELECT * FROM submissions WHERE galleryID = %d"%(gID)).fetchall():
        subs += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "imgTextData": str(sub[3]), "miniImageTextData": str(sub[4]), "script": str(sub[5]), "time": str(sub[6])} ]
    return subs

#get all submissions from a particular student
def getAllWork(sID):
    work = []
    for sub in c.execute("SELECT * FROM submissions WHERE sID = '%s'"%(sID)).fetchall():
        work += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "img": str(sub[3]), "script": str(sub[4]), "time": str(sub[5])} ]
    return work

#get student Info from a given student id
def getStudentInfo(sID):
    studentInfo = []
    for student in c.execute("SELECT * FROM students WHERE id = '%s'"%(sID)).fetchall():
        studentInfo += [ {"displayName": student[0], "year": student[2]}]
    return studentInfo

#SETTING UP SAMPLE DATABASES WITH INFO
'''
createStudents()
createGalleries()
createSubmissions()

addStudent("Constantine Athanitis", "pass1234", 2017, "cathanitis")
addStudent("Sebastian Cain", "pass5678", 2017, "scain")
addStudent("Elias Milborn", "1234pass", 2017, "emilborn")
addStudent("Nalanda Sharadjaya", "5678pass", 2017, "nsharadjaya")

addAssignment("Circle")
addAssignment("Square")

addSubmission(getAssignmentID("Circle"), "My Circle", "cathanitis", "image txt","miniImage text", "script txt", "TIME")
addSubmission(getAssignmentID("Circle"), "Circle!!", "scain", "image txt","miniImage text", "script txt", "TIME")
addSubmission(getAssignmentID("Circle"), "Circle :O", "emilborn", "image txt","mini image text", "script txt", "TIME")
addSubmission(getAssignmentID("Circle"), "Circle", "nsharadjaya", "image txt", "miniimage text", "script txt", "TIME")
addSubmission(getAssignmentID("Square"), "My Square", "cathanitis", "image txt","mini image text", "script txt", "TIME")
addSubmission(getAssignmentID("Square"), "Square!!", "scain", "image txt","mini image text", "script txt", "TIME")
addSubmission(getAssignmentID("Square"), "Square :O", "emilborn", "image txt","mini image text", "script txt", "TIME")
addSubmission(getAssignmentID("Square"), "Square", "nsharadjaya", "image txt","miniImage text", "script txt", "TIME")
'''
print getAllGalleries()
print "----------------------------"
print getAllSubmissions(1)
print "----------------------------"
print getAllSubmissions(2)
print "----------------------------"
print getAllWork("cathanitis")
print "----------------------------"
print getAllWork("scain")
print "----------------------------"
print getAllWork("emilborn")
print "----------------------------"
print getAllWork("nsharadjaya")
print "----------------------------"
print getStudentInfo("scain")
print "----------------------------"
print getStudentInfo("emilborn")

