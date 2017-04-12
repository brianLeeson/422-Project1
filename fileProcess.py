"""
Author(s): Brian Leeson

"""

import Student
import csv
def timestamp(meeting_time):
	'''
	input -> string, representation of a datetime meeting time
	output -> datetime object
	'''
	#TODO determine if we need this function at all
	return

def process(fileName):
	"""
	This function opens a csv 'fileName',
	parses student info from the file,
	and creates instances of the Student class.
	returns a list of students 
	TODO (? Is this return we want?) 
	:param fileName: string of the file name in the local directory
	:return: a list (?) of student instances
	"""
	studentList = []
	with open(fileName, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in csvfile:
			print(row['Student Name'])
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
			     
			student = Student.Student("FAKE NAME", ["FAKE CRITERIA"])
			studentList.append(student)

	return studentList

#----------------------Sandbox Area--------------------------------------
if __name__=='__main__':
	process('example_survey_answer.csv')
