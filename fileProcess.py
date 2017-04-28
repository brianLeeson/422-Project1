"""
Author(s): Jamie Zimmerman
This file is responsible for parsing csv on import into students for the gui to use.
Then, when sorting is complete, this file handles exporting data back to a csv.

This module is responsible for the intake of survey data and export of optimal team decisions.

process method intakes a csv file. No active other part of our program is currently responsible 
for collecting that data besides a Google survey that is provided in the repo for the user when 
they download and install our app. It is critical that the teacher use the Google Survey provided 
as the headers in it are hard-coded in this module. Using the csv library, the process method 
reads the appropriate data and instantiates the necessary objects. Each row in the survey results 
is one student's answers, so for each row we instantiate a Student object.

export method gets a list of final team objects and writes them to a csv file, provided for the 
teacher's use. Each row is a Team, and it lists not only the students in it but each student's 
meeting time/coding experience and the team's matching qualities. By providing more granular 
information, the teacher can look realistically at the teams and then personally make changes to 
Teams as he/she deems fit. The algorithm performs well, but can't read the mind of the teacher. 
For example if the teacher knows that certain students despise each other, then he/she can manually 
check if they are on a team, and if so, make changes, with more granular information on hand.

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
		survey_headers = ['Python experience', 'Java experience', 'Javascript experience', 'C experience',
				'C++ experience', 'PHP experience', 'HTML experience', 'SQL experience',
				'Bash/Unix experience']

		for row in reader:
			# parse time availability data
			mon = row['Monday']
			tues = row['Tuesday']
			wed = row['Wednesday']
			thurs = row['Thursday']
			fri = row['Friday']

			# get student's requested groupmates
			requests = row["Desired Teammates DuckIDs (separated by ';')"].split(';')
			# create a student object
			student = Student(row['Student Name'], row['Your DuckID'])
			for i in range(9):
				student.setCodeExperience(languages[i], int(row[survey_headers[i]]))
			#to add non-binary listing of student's time availability
			student.add_to_time_list('Monday ' + mon)
			student.add_to_time_list('Tuesday ' + tues)
			student.add_to_time_list('Wednesday  ' + wed)
			student.add_to_time_list('Thursday ' + thurs)
			student.add_to_time_list('Friday ' + fri)
			student.setAvailability(create_time_chart([mon, tues, wed, thurs, fri]))
			student.setRequests(requests)  # It's ok that this is just a list of duckIDs and not student objects

			studentList.append(student)

	return studentList


# helper function to process student availability into binary representation
def create_time_chart(day_availability_list):
	"""
	input  - list of day's time slots, ex: ["10:00-12:00;2:00-4:00", "2:00-4:00;4:00-6:00", "10:00-12:00;4:00-6:00", 
		"None", "10:00-12:00;2:00-4:00"]
		the first item in the list is Monday, then Tuesday, etc... (the function zips this with in-order days so that 
		the data is not scrambled)  
		within each 'day' is a semicolon separated list of available times slots
	this function parses that availability into a binary representation
	output - dictionary - entire dictionary representing student's availability
		key: days (Monday, Tuesday, etc.)
		value: a list of 0's and 1's, which indicates which times slots are open for that student
		ex: "Monday":[0, 1, 1, 0, 0] means that the student is available on Monday from 12:00-2:00& 2:00-4:00
		the list should only be 5 spaces long, representing 4 time slots(10-12, 12-2, 2-4, 4-6) and None, meaning 
		no time available example usage: student.setAvailability(create_time_chart(day_availability_list))
	"""

	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	pre_chart = dict(zip(days, day_availability_list))
	chart = dict()
	for day, daytimes in pre_chart.items():
		times = daytimes.split(';')
		new_li = [0 for i in range(5)]
		for slot in times:
			if slot == "10:00 - 12:00":
				new_li[0] = 1
			elif slot == "12:00 - 2:00":
				new_li[1] = 1
			elif slot == "2:00 - 4:00":
				new_li[2] = 1
			elif slot == "4:00 - 6:00":
				new_li[3] = 1
			else:  # No available time
				new_li[0:] = [0 for i in range(5)]
		chart[day] = new_li
	return chart


def export(decided_teams):
	"""
	input-> list of Team objects
	function writes teams as a csv to cwd
	Each team is a new header in the csv file for readability. For example, the first row has the team number,
	a header for the student's availability, a header for the student's best programming languages, a header 
	describing the team's matching meeting times, and a header listing the team's matching programming languages. 
	For example, in the csv file, say there are two teams. When the file is opened in Excel, it looks like:
	
	<Team 1> <student time availability> <student coding languages> <team's meeting times: ['Monday 12:00 - 2:00', 'Thursday 4:00 - 6:00']> <team languages: ['PHP', 'SQL']
	Susie Shunpike ['Monday 12:00 - 2:00', 'Thursday 4:00 - 6:00'] ['PHP', 'SQL', 'Java', 'C']
	Holden Morocco ['Monday 12:00 - 2:00', 'Thursday 4:00 - 6:00', 'Friday 10:00 - 12:00'] ['PHP', 'SQL', 'Bash/Unix']
	Annabel Lee []['Monday 12:00 - 2:00', 'Thursday 4:00 - 6:00', 'Friday 2:00 - 4:00'] ['PHP', 'SQL', 'Javascript']
	
	<Team 2> ...


	and so on. Having additional information is useful for the teacher so that they can see exactly when teams 
	can meet and what their best skills are. Morever, if the teacher wants to make manual changes to the teams, 
	the information is right on hand about when a student is free.

	
	output-> None, writing the file is a side effect
	"""
	with open('team_decisions.csv', 'w') as out_file:
		i = 1
		for team in decided_teams:
			fieldnames = ['Team {}'.format(i),
					'student time availability',
					'student coding languages',
					"team's meeting times: {}". format(str(team.get_time_slots())),
					'team languages: {}'.format(team.get_common_langs())]
			writer = csv.DictWriter(out_file, fieldnames=fieldnames)
			writer.writeheader()
			for guy in team.getMemberList():
				writer.writerow({'Team {}'.format(i): guy.getName(),
						'student time availability': guy.get_time_list(),
						'student coding languages': guy.getLanguages()})
			i += 1
	return None


# ----------------------Sandbox Area--------------------------------------
if __name__ == '__main__':
	# THIS CODE NEVER NEEDS TO BE SAVED, JUST A WORKSPACE AREA
	stu_li = process('test_cases/one_extra.csv')
	for guy in stu_li:
		print(guy)
		print(guy.getAvailability())
		print(guy.getCodeExperience())
		print(guy.getTeammates())
		print(guy.get_time_list())
	team1 = Team(1)
	team1.setMemberList(stu_li[0:3])
	team2 = Team(2)
	team2.setMemberList(stu_li[3:6])
	team3 = Team(3)
	team3.setMemberList(stu_li[6:10])
	export([team1, team2, team3])
