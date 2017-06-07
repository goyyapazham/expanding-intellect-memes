import sqlite3, os

filename = "utils/data.db"
#filename = "data.db"

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
    db.commit()
    
#create submissions table (only use once!)
def createSubmissions():
    c.execute("CREATE TABLE IF NOT EXISTS submissions (galleryID INTEGER, title TEXT, sID TEXT, imagePath TEXT, miniImagePath TEXT, script TEXT, time TEXT, subID INTEGER PRIMARY KEY AUTOINCREMENT)")
    db.commit()
    
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
    q = "INSERT INTO submissions VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', NULL)"%(gID, title, sID, img, mini, script, time)
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
        subs += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "imgPath": str(sub[3]), "miniImagePath": str(sub[4]), "script": str(sub[5]), "time": str(sub[6]), "subID": str(sub[7])} ]
    return subs

#get all submissions from a particular student
def getAllWork(sID):
    work = []
    for sub in c.execute("SELECT * FROM submissions WHERE sID = '%s'"%(sID)).fetchall():
        work += [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "imgPath": str(sub[3]), "miniImagePath": str(sub[4]), "script": str(sub[5]), "time": str(sub[6]), "subID": str(sub[7])} ]
    return work

#get student Info from a given student id
def getStudentInfo(sID):
    studentInfo = []
    for student in c.execute("SELECT * FROM students WHERE id = '%s'"%(sID)).fetchall():
        studentInfo += [ {"displayName": student[0], "year": student[2]}]
    return studentInfo

def getAllStudents():
    students = []
    for student in c.execute("SELECT * FROM students").fetchall():
        students += [{"displayName": student[0], "studentID":student[1], "year": student[2]}]
    return students

def deleteGallery(gID):
    c.execute("DELETE FROM galleries WHERE id = %d"%(gID))
    #deleting the image files first
    for path in c.execute("SELECT imagePath FROM submissions WHERE galleryID = %d"%(gID)).fetchall():
        pathString = "rm static/" + path[0]
        os.system(pathString)
    for path in c.execute("SELECT miniImagePath FROM submissions WHERE galleryID = %d"%(gID)).fetchall():
        pathString = "rm static/" + path[0]
        os.system(pathString)
    c.execute("DELETE FROM submissions WHERE galleryID = %d"%(gID))
    db.commit()

def getSubmission(subID):
    #should only output one dictionary, because each subID is unique
    submission = []
    for sub in c.execute("SELECT * FROM submissions WHERE subID = '%s'"%(subID)).fetchall():
        submission +=  [ {"gID": sub[0], "title": str(sub[1]), "sID": str(sub[2]), "imgPath": str(sub[3]), "miniImagePath": str(sub[4]), "script": str(sub[5]), "time": str(sub[6]), "subID": str(sub[7])} ]
    return submission

    
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

addAssignment("Triangle")
addSubmission(getAssignmentID("Triangle"), "My Triangle", "cathanitis", "image path","miniImage path", "script txt", "TIME")
addSubmission(getAssignmentID("Triangle"), "Triangle!!", "scain", "image path","miniImage path", "script txt", "TIME")
addSubmission(getAssignmentID("Triangle"), "Triangle :O", "emilborn", "image path","mini image path", "script txt", "TIME")
addSubmission(getAssignmentID("Triangle"), "Triangle", "nsharadjaya", "image path", "miniimage path", "script txt", "TIME")
'''
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


'''
