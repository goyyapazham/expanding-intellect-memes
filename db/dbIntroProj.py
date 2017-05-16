from pymongo import MongoClient
import csv

#change from local server to Homer server
#server = MongoClient("127.0.0.1")
#server = MongoClient('homer.stuy.edu')
server = MongoClient("149.89.150.100")

#creating the database
db = server.dbSample


studentInfoCollection = db.studentInfo
assignmentsCollection = db.assignments


def submitToStudents(name, password, year):
    num = db.studentInfoCollection.count()
    print num
    currentID = num + 1
    dStudent = {"name":name, "password":password, "studentID":currentID, "year":year}

    studentInfoCollection.insert_one(dStudent)


def deleteFromStudents(id):
    db.studentInfoCollection.deleteOne({"studentID":id})
    
def displayStudentInfo():
    for student in studentInfoCollection.find():
        print student

submitToStudents("Costa", "pass1", 2017)
submitToStudents("Nala", "pass2", 2016)
submitToStudents("Elias", "pass3", 2017)
displayStudentInfo()
deleteFromStudents(2)
displayStudentInfo()        


"""
#creating the collection
studentCollection = db.students

'''Commented out so that we don't have any more additions
to the database'''
#opening up the csv/data files
fObjP = open("peeps.csv")
people=csv.DictReader(fObjP)
for i in people:
    #creates a dictionary of the peeps data: name, age, id
    dPeeps = {"name":i["name"], "age":i["age"], "id":i["id"]}
    fObjC = open("courses.csv")
    courses = csv.DictReader(fObjC)
    
    for j in courses:
        #if id from peeps data matches with id from courses data,
        #add the mark for the specific course to the dictionary
        if j["id"] == dPeeps["id"]:
            dPeeps[j["code"]]= j["mark"]
            
    print dPeeps
    #insert the dictionary/document into the collection
    studentCollection.insert_one(dPeeps)


def displayInfo():
	for student in studentCollection.find():
		#print student
		sum = 0		
		nOC = 0 #number of courses
		if "softdev" in student:
			sum = sum + int(student["softdev"])
			nOC = nOC + 1
		if "systems" in student:
			sum = sum + int(student["systems"])
			nOC = nOC + 1
		if "greatbooks" in student:
			sum = sum + int(student["greatbooks"])
			nOC = nOC + 1
		if "ceramics" in student:
			sum = sum + int(student["ceramics"])
			nOC = nOC + 1

		average = sum / nOC

		
		print "Name: "+student["name"]
		print "ID: "+student["id"]
		print "Average: "+ str(average)
    		print "----------------------"

displayInfo()

print
print
print

teacherCollection = db.teachers

fObjT = open("teachers.csv")
teachers = csv.DictReader(fObjT)

for i in teachers:	
	dTeacher = {"teacher":i["teacher"], "class":i["code"], "students":[]}
	
	for student in studentCollection.find():
		if i["code"] in student:
			dTeacher["students"].append(student["id"])
	#the list contains the id numbers, but in tuple form
	#ie [u'1',u'2',u'6']
	print dTeacher
	print	
	print
teacherCollection.insert_one(dTeacher)
"""
