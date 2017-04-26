"""
Author(s): Jamie Zimmerman

This module is responsible for the intake of survey data and export of optimal team decisions.

process method intakes a csv file. No active other part of our program is currently responsible for collecting that data besides a Google survey that is provided in the repo for the user when they download and install our app. It is critical that the teacher use the Google Survey provided as the headers in it are hard-coded in this module. Using the csv library, the process method reads the appropriate data and instantiates the necessary objects. Each row in the survey results is one student's answers, so for each row we instantiate a Student object.

export method gets a list of final team objects and writes them to a csv file, provided for the teacher's use. Each row is a Team, and it lists not only the students in it but each student's meeting time/coding experience and the team's matching qualities. By providing more granular information, the teacher can look realistically at the teams and then personally make changes to Teams as he/she deems fit. The algorithm performs well, but can't read the mind of the teacher. For example if the teacher knows that certain students despise each other, then he/she can manually check if they are on a team, and if so, make changes, with more granular information on hand.

"""

from Student import Student  # from module import class
from Team import Team
import csv


def process(fileName):
	"""
	input -> string of a csv file, ex: '422_Project_Template.csv'
	reads the file using csv dictionary reader
	takes the information from each row (which represents a student)
	and creates a student object
	output -> a list of student Objects, which can then be attached to the Classroom instance.
	"""
	studentList = []
	with open(fileName, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		languages = ['Python', 'Java', 'Javascript', 'C', 'C++', 'PHP', 'HTML', 'SQL', 'Bash/Unix']
		survey_headers = ['Python experience', 'Java experience', 'Javascript experience', 'C experience', 'C++ experience', 'PHP experience', 'HTML experience', 'SQL experience', 'Bash/Unix experience']
		
		for row in reader:
			#parse time availability data
			mon = row['Monday']
			tues = row['Tuesday']
			wed = row['Wednesday']
			thurs = row['Thursday']
			fri = row['Friday']

			#get student's requested groupmates
			requests = row["Desired Teammates DuckIDs (separated by ';')"].split(';')

			#create a student object
			student = Student(row['Student Name'], row['Your DuckID'])
			for i in range(9):  # the provided survey lists the 9 major languages most applicable/favorable to a group of upperdiv CS students
				student.setCodeExperience(languages[i], int(row[survey_headers[i]]))
				#print('{} for tool {} has skill {}'.format(student.getName(), languages[i], row[survey_headers[i]]))

			student.setAvailability(create_time_chart([mon, tues, wed, thurs, fri]))
			student.setRequests(requests) # It's ok that this is just a list of duckIDs and not student objects

			studentList.append(student)

	return studentList


#helper function to process student availability into binary representation
def create_time_chart(day_availability_list):
	"""
	input  - list of day's time slots, ex: ["10:00-12:00;2:00-4:00", "2:00-4:00;4:00-6:00", "10:00-12:00;4:00-6:00", "None", "10:00-12:00;2:00-4:00"]
		the first item in the list is Monday, then Tuesday, etc... (the function zips this with in-order days so that the data is not scrambled)
		within each 'day' is a semicolon separated list of available times slots
	this function parses that availability into a binary representation
	output - dictionary - entire dictionary representing student's availability
		key: days (Monday, Tuesday, etc.)
		value: a list of 0's and 1's, which indicates which times slots are open for that student
		ex: "Monday":[0, 1, 1, 0, 0] means that the student is available on Monday from 12:00-2:00& 2:00-4:00
		the list should only be 5 spaces long, representing 4 time slots(10-12, 12-2, 2-4, 4-6) and None, meaning no time available
		example usage: student.setAvailability(create_time_chart(day_availability_list))
	"""
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
			else:  # No available time
				new_li[0:] = [0 for i in range(5)]
		chart[day] = new_li
	return chart


def export(decided_teams):
	"""
	input-> list of Team objects
	function writes teams as a csv to cwd
	output-> None, writing the file is a side effect
	"""
	with open('team_decisions.csv', 'w') as csvfile:
		fieldnames = ['Team Number', 'Student 1', 'Student 2', 'Student 3', 'Student 4']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		i = 1
		for team in decided_teams:
			teammates = team.getMemberList()
			entry = {'Team Number': i, 'Student 1': teammates[0]}
			if len(teammates) >= 2:
				entry['Student 2']= teammates[1]
				if len(teammates) >= 3:
					entry['Student 3']= teammates[2]
					if len(teammates) >= 4:
						entry['Student 4']= teammates[3]
			writer.writerow(entry)
			i += 1
	
	return None

# ----------------------Sandbox Area--------------------------------------
if __name__ == '__main__':
	# THIS CODE NEVER NEEDS TO BE SAVED, JUST A WORKSPACE AREA
	stu_li = process('fake_422_data.csv')
	for guy in stu_li:
		print(guy)
		print(guy.getAvailability())
		print(guy.getCodeExperience())
		print(guy.getTeammates())
	team1 = Team(1)
	team1.setMemberList(stu_li[0:3])
	team2 = Team(2)
	team2.setMemberList(stu_li[3:6])
	team3 = Team(3)
	team3.setMemberList(stu_li[6:10])
	export([team1, team2, team3])
