"""
Author(s): Jamie Zimmerman

"""

from Student import Student #from module import class
import csv
def timestamp(meeting_time):
	'''
	input -> string, representation of a datetime meeting time
	output -> datetime object
	'''
	#TODO determine if we need this function at all
	return

def process(fileName):
	'''
	input -> string of a csv file
	reads the file using csv dictionary reader
	takes the information from each row (which represents a student)
	and creates a student object
	'''
	studentList = []
	with open(fileName, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			email = row['Username']
			name = row['Student Name']
			pyth = row['Python experience']
			java = row['Java experience']
			js = row['Javascript experience']
			c = row['C experience']
			cpp = row['C++ experience']
			php = row['PHP experience']
			html = row['HTML experience']
			sql = row['SQL experience']
			bash = row['Bash/Unix experience']

			mon =  row['Monday']
			tues =  row['Tuesday']
			wed = row['Wednesday']
			thurs = row['Thursday']
			fri = row['Friday']
			
			requests = row["Desired Teammates @uoregon.edu emails (separated by ';')"]

			student = Student(name, email)
			student.setCodeExperience('Python', pyth)
			student.setCodeExperience('Java', java)
			student.setCodeExperience('C', c)
			student.setCodeExperience('C++', cpp)
			student.setCodeExperience('PHP', php)
			student.setCodeExperience('HTML', html)
			student.setCodeExperience('SQL', sql)
			student.setCodeExperience('Bash/Unix', bash)
			
			student.setAvailability('Monday', mon)
			student.setAvailability('Tuesday', tues)
			student.setAvailability('Wednesday', wed)
			student.setAvailability('Thursday', thurs)
			student.setAvailability('Friday', fri)

			#TODO figure out how to create student objects from request list - these need to be added to the students teammate list
			studentList.append(student)

	return studentList

#----------------------Sandbox Area--------------------------------------
if __name__=='__main__':
	for guy in process('example_survey_answer.csv'):
		print(guy)
