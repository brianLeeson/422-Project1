"""
Author(s): Jamie Zimmerman

"""

from Student import Student  # from module import class
import csv


def timestamp(meeting_time):
	"""
	input -> string, representation of a datetime meeting time
	output -> datetime object
	"""

	# TODO determine if we need this function at all

	return


def process(fileName):
	"""
	input -> string of a csv file
	reads the file using csv dictionary reader
	takes the information from each row (which represents a student)
	and creates a student object
	"""
	studentList = []
	with open(fileName, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			duckID = row['Your DuckID']
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

			mon = row['Monday']
			tues = row['Tuesday']
			wed = row['Wednesday']
			thurs = row['Thursday']
			fri = row['Friday']
			
			requests = row["Desired Teammates DuckIDs (separated by ';')"]

			student = Student(name, duckID)
			student.setCodeExperience('Python', pyth)
			student.setCodeExperience('Java', java)
			student.setCodeExperience('Javascript', js)
			student.setCodeExperience('C', c)
			student.setCodeExperience('C++', cpp)
			student.setCodeExperience('PHP', php)
			student.setCodeExperience('HTML', html)
			student.setCodeExperience('SQL', sql)
			student.setCodeExperience('Bash/Unix', bash)
			
			student.setAvailability(create_time_chart([mon, tues, wed, thurs, fri]))

			# TODO figure out how to create student objects from request list - these need to be added to the students teammate list
			studentList.append(student)

	return studentList


#helper function to process student availability into binary representation
def create_time_chart(day_availability_list):
	'''
	input  - list of day's time slots, ex: ["10:00-12:00;2:00-4:00", "2:00-4:00;4:00-6:00", "10:00-12:00;4:00-6:00", "None", "10:00-12:00;2:00-4:00"]
		the first item in the list is Monday, then Tuesday, etc... (the function zips this with in-order days so that the data is not scrambled)
		within each 'day' is a semicolon separated list of available times slots
	this function parses that availability into a binary representation
	output - dictionary
		key: days (Monday, Tuesday, etc.)
		value: a list of 0's and 1's, which indicates which times slots are open for that student
		ex: "Monday":[0, 1, 1, 0, 0] means that the student is available on Monday from 12:00-2:00& 2:00-4:00
		the list should only be 5 spaces long, representing 4 time slots(10-12, 12-2, 2-4, 4-6) and None, meaning no time available
	'''
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	pre_chart = dict(zip(days, day_availability_list))
	chart = dict()
	for day, daytimes in pre_chart.items():
		times = daytimes.split(';')
		new_li = [0 for i in range(5)]
		for slot in times:
			if slot == "10:00 - 12:00":
				new_li[0]=1
			elif slot == "12:00 - 2:00":
				new_li[1]=1
			elif slot == "2:00 - 4:00":
				new_li[2]=1
			elif slot == "4:00 - 6:00":
				new_li[3]=1
			else: #No available time
				new_li[4]=1
				new_li[0:4] = [0 for i in range(4)]
		chart[day] = new_li
	return chart


def export(decided_teams):
	"""
	THIS FUNCTION ASSUMES THAT THE INPUT IS A LIST OF TEAM OBJECTS***
	function writes teams as a csv to cwd
	"""
	with open('team_decisions.csv', 'w') as csvfile:
		fieldnames = ['Team Number', 'Student 1', 'Student 2', 'Student 3']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		i = 1
		for team in decided_teams:
			#TODO print team's UID, not just a random number
			teammates = team.getMemberList()
			writer.writerow({'Team Number':i, 'Student 1':teammates[0], 'Student 2':teammates[1], 'Student 3':teammates[2]})
			i += 1
	
	return None

# ----------------------Sandbox Area--------------------------------------
if __name__ == '__main__':
	'''for guy in process('422_Project1_Template.csv'):
		print(guy)
		print(guy.getAvailability())
	b_chart = ["10:00-12:00;2:00-4:00", "2:00-4:00;4:00-6:00", "10:00-12:00;4:00-6:00", "None", "10:00-12:00;2:00-4:00"]
	'''
	decided = process('422_Project1_Template.csv')
	
