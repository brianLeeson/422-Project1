"""
Author(s): Brian Leeson + Jamie Zimmerman + Amie Corso

"""


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	# NOTE: I think that any attribute of Student that could be a list should be a tuple.
	# There might be some aliasing issues we could nip in the bud if we chose tuples
	# from Amie:  only note on this is that the potential_teams attritube needs to be mutable (list)

	def __init__(self, name, duckID):
		self.name = name
		self.duckID = duckID  # Use this attribute as a unique identifier

		self.overallExperience = 0  # overall experience score - how many upper div CS classes completed
		self.codeExperience = {
			'Python': 0, 'Java': 0, 'Javascript': 0, 'C': 0, 'C++': 0,
			'PHP': 0, 'HTML': 0, 'SQL': 0,'Bash/Unix': 0}
		# values are list of 0s and 1s representing true availability for time slots
		self.availability = {
								'Monday': [],
								'Tuesday': [],
								'Wednesday': [],
								'Thursday': [],
								'Friday': []
		}
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

	def getOverallExperience(self):
		return self.overallExperience

	def setOverallExperience(self, exp):
		self.overallExperience = exp
		return None

	def getCodeExperience(self):
		"""
		output -> dictionary mapping languages to integer rating of skill
		ex: dict = {'Python': 5 ... and so on}
		"""
		return self.codeExperience

	def setCodeExperience(self, tool, capability):
		"""
		input -> tool - string of a coding lanugage i.e.: 'Python'
			capability - string OR int that is integer rating of skill
		this function sets the student's particular language skill to a rating, casting the rating to an int as a safety measure
		'"""
		self.codeExperience[tool] = capability
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

	def setTeammates(self, buddies):
		"""
		input: buddies is a list of strings, the duck ID's of desired teammates
		"""
		self.teammates = buddies
		return None

	def addTeammate(self, buddy):
		self.teammates.append(buddy)
		return None

	def getTeammates(self):
		return self.teammates


# -----------------------------------Sandbox Area -------------------------------------------------#
if __name__ == '__main__':
	student = Student('Brian', 'brian@brian.com')
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

	# testing requested teammates list
	friend = Student('Jamie', 'jamie@yellow.edu')
	student.setTeammates(friend)
	for s in student.getTeammates():
		print(s)
	print(student)
