"""
Author(s): Brian Leeson

"""

import Student

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
	with open(fileName, "r") as csvFile:
		studentList = []
		for line in csvFile:
			# TODO parse line. we need to define what our google forms will be

			student = Student.Student("FAKE NAME", ["FAKE CRITERIA"])
			studentList.append(student)

	return studentList


