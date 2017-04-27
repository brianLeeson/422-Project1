"""
Author(s): Brian Leeson + Jamie Zimmerman + Amie Corso

Student.py holds a class Student that serves as a way to store data in main memory. We created our own object type to hold information about each student, the most important information being their name, their meeting time freedom, and their programming language skill. Each instantiation represents a student in a CIS422 course. The information is gathered via a Google survey.

name
duckID -> specific to each student
codeExperience -> a dictionary mapping a particular language to approximate rated skill
availability -> dictionary mapping days to a list of zeros and ones, which correspond to the time slots 10:00-12:00, 12:00-2:00, 2:00-4:00, and 4:00-6:00
requests -> duckIDs of desired teammates
potential_teams -> a list of Team objects in which a student could belong on - these slowly disappear as the algorithm determines that the Team is unviable.
assignedTeam -> whichever Team the student ends up on

Notes for fellow/future developers:
Read the comments and docstrings - you don't need to know how the functions or methods work or what attribute methods serve for.
In general, this module has little to it besides attributes and getter/setter methods. It is mostly used as a container because no other data object served our purposes as well as building our own.

"""


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	def __init__(self, name, duckID):
		self.name = name
		self.duckID = duckID  # Use this attribute as a unique identifier

		self.codeExperience = {'Python': 0, 'Java': 0, 'Javascript': 0, 'C': 0, 'C++': 0, 'PHP': 0, 'HTML': 0, 'SQL': 0, 'Bash/Unix': 0}
		self.availability = {'Monday': [], #values are list of 0s and 1s representing true availability for time slots 
					'Tuesday': [],
					'Wednesday': [],
					'Thursday': [],
					'Friday': []}
		self.time_list = [] #non-binary representation of available time, each entry is a string of the day and hours available
		self.requests = []  # list of strings - duckIDs of desired teammates
		self.potential_teams = []  # used during sorting process to keep track of which teams on which a student COULD appear
		self.assignedTeam = None  # keeps track during sorting process of which team a student is associated with
		# final once the sorting process is complete
		self.teammates = []

	def sort_potential_teams(self):
		self.potential_teams.sort()
		self.potential_teams.reverse()
		return None

	def __str__(self):
		return self.getName()

	def __cmp__(self, other):
		return self.getduckID() == other.getduckID()

	def __lt__(self, other):
		return len(self.potential_teams) < len(other.potential_teams)

	def __le__(self, other):
		return len(self.potential_teams) <= len(other.potential_teams)

	def __gt__(self, other):
		return len(self.potential_teams) > len(other.potential_teams)

	def __ge__(self, other):
		return len(self.potential_teams) >= len(other.potential_teams)

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
		return None

	def getduckID(self):
		return self.duckID

	def setduckID(self, duckID):
		self.duckID = duckID
		return None

	def setRequests(self, requests):
		self.requests = requests
		return None

	def getRequests(self):
		return self.requests

	def getCodeExperience(self):
		"""
		output -> dictionary mapping languages to integer rating of skill
		ex: dict = {'Python': 5 ... and so on}
		"""
		return self.codeExperience
	

	def getLanguages(self):
		'''
		output -> list of student's proficient coding languages, i.e. self rated skill is 3 or higher
		'''
		languages = []
		for language, skill in self.codeExperience.items():
			if skill > 2:
				languages.append(language)
		return languages

	def setCodeExperience(self, tool, capability):
		"""
		input -> tool - string of a coding lanugage i.e.: 'Python'
			capability - string OR int that is integer rating of skill
		this function sets the student's particular language skill to a rating, casting the rating to an int as a safety measure
<<<<<<< HEAD
		'''
		self.codeExperience[tool] = int(capability)
=======
		'"""
		self.codeExperience[tool] = capability
>>>>>>> e5ce343fadd0ab55a98334c47c2daf0c559cd479
		return None

	def getAvailability(self):
		"""
		output -> dictionary representation of student's availability chart
			may want to add specifying parameters that narrow down for a certain day
		"""
		return self.availability

	def setAvailability(self, graph):
		"""
		input -> graph is an entire dictionary representing the student's entire weeklong availability
		"""
		self.availability = graph
		return None

<<<<<<< HEAD
	def get_time_list(self):
		return self.time_list

	def add_to_time_list(self, daytime):
		self.time_list.append(daytime)
		return None

=======
>>>>>>> e5ce343fadd0ab55a98334c47c2daf0c559cd479
	def setTeammates(self, buddies):
		"""
		input: buddies is a list of strings, the duck ID's of desired teammates
		"""
		self.teammates = buddies
		return None

	def addTeammate(self, buddy):
		'''
		input is a string, a singular duckID of one person requested
		'''
		self.teammates.append(buddy)
		return None

	def getTeammates(self):
		return self.teammates


# -----------------------------------Sandbox Area -------------------------------------------------#
# This code here was used for testing purposes during initial development. It does not need to be saved.
if __name__ == '__main__':
	student = Student('Brian', 'brian@brian.com')
<<<<<<< HEAD
	student.setCodeExperience('Python', 5)
	student.setCodeExperience('Java', 2)
	student.setCodeExperience('Javascript', 4)
	student.setCodeExperience('C', 3)
	print(student.getLanguages())
	student.add_to_time_list('Monday 12:00 - 2:00')
	student.add_to_time_list('Monday 2:00 - 4:00')
	print(student.get_time_list())
	
=======
	student.setCodeExperience('Python', 8)
	print(student.getCodeExperience())
	student.setOverallExperience(4)
	print('{} is this qualified: {}'.format(student.getName(), student.getOverallExperience()))

	# testing availability attributes
	print(student.getAvailability())
	student.setAvailability('Thursday')
	print(student.getAvailability())
	student.setAvailability('Thursday')
	print(student.getAvailability())

>>>>>>> e5ce343fadd0ab55a98334c47c2daf0c559cd479
	# testing requested teammates list
	friend = Student('Jamie', 'jamie@yellow.edu')
	student.setTeammates(friend)
	#for s in student.getTeammates():
	#	print(s)
	print(student)
