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
    c.execute("CREATE TABLE IF NOT EXISTS submissions (galleryID INTEGER, title TEXT, sID TEXT, imageData TEXT, script TEXT)")

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
def addSubmission(gID, title, sID, img, script):
    q = "INSERT INTO submissions VALUES (%d, '%s', '%s', '%s', '%s')"%(gID, title, sID, img, script)
    c.execute(q)
    db.commit()

## RETURN DICTIONARIES

#get all assignments
def getAllAssignments():
    assignments = []
    for assignment in c.execute("SELECT * FROM galleries").fetchall():
        assignments += [ {"name": str(assignment[0]), "id": assignment[1]} ]
    return assignments
    
#get all submissions for an assignment
def getAllSubmissions(gID):
    subs = []
    for sub in c.execute("SELECT * FROM submissions WHERE galleryID = %d"%(gID)).fetchall():
        subs += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "img": str(sub[3]), "script": str(sub[4])} ]
    return subs

#get all submissions from a particular student
def getAllWork(sID):
    work = []
    for sub in c.execute("SELECT * FROM submissions WHERE sID = '%s'"%(sID)).fetchall():
        work += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "img": str(sub[3]), "script": str(sub[4])} ]
    return work

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

addSubmission(getAssignmentID("Circle"), "My Circle", "cathanitis", "image txt", "script txt")
addSubmission(getAssignmentID("Circle"), "Circle!!", "scain", "image txt", "script txt")
addSubmission(getAssignmentID("Circle"), "Circle :O", "emilborn", "image txt", "script txt")
addSubmission(getAssignmentID("Circle"), "Circle", "nsharadjaya", "image txt", "script txt")
addSubmission(getAssignmentID("Square"), "My Square", "cathanitis", "image txt", "script txt")
addSubmission(getAssignmentID("Square"), "Square!!", "scain", "image txt", "script txt")
addSubmission(getAssignmentID("Square"), "Square :O", "emilborn", "image txt", "script txt")
addSubmission(getAssignmentID("Square"), "Square", "nsharadjaya", "image txt", "script txt")
'''

print getAllAssignments()
print getAllSubmissions(1)
print getAllSubmissions(2)
print getAllWork("cathanitis")
print getAllWork("scain")
print getAllWork("emilborn")
print getAllWork("nsharadjaya")
