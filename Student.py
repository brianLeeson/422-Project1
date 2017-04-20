"""
Author(s): Brian Leeson + Jamie Zimmerman + Amie Corso

"""
import datetime


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	# NOTE: I think that any attribute of Student that could be a list should be a tuple.
	# There might be some aliasing issues we could nip in the bud if we chose tuples
	# from Amie:  only note on this is that the potential_teams attritube needs to be mutable (list)

	def __init__(self, name, email):
		self.name = name
		self.duckID = duckID #Use this attribute as a unique identifier

		self.overallExperience = 0  # overall experience score - how many upper div CS classes completed
		self.codeExperience = {'Python': 0,
							'Java': 0,
							'JavaScript': 0,
							'C': 0,
							'C++': 0,
							'PHP': 0,
							'HTML': 0,
							'SQL': 0,
							'Bash/Unix': 0}
		self.availability = {'Monday': [],  # the value is a list of datetime objects (possibly)
					'Tuesday': [],
					'Wednesday': [],
					'Thursday': [],
					'Friday': []}
		self.teammates = []  # list of student Objects - recursive relation
		self.potential_teams = [] # used during sorting process to keep track of which teams on which a student COULD appear
		self.assignedTeam = None  # keeps track during sorting process of which team a student is associated with
								  # final once the sorting process is complete

	def sort_potential_teams(self):
		self.potential_teams.sort()
		self.potential_teams.reverse()
		return None

	def __str__(self):
		# TODO fix this usage - throws a type error because it can't print int type (from UID)
		# example, when you call print(student)
		return self.getName()

	def __cmp__(self, other):
		return self.getUID() == other.getUID()

	def __lt__(self, other):
		return len(self.potential_teams) < len(other.potential_teams)

	def __le__(self, other):
		return len(self.potential_teams) <= len(other.potential_teams)

	def __gt__(self, other):
		return len(self.potential_teams) > len(other.potential_teams)

	def __ge__(self, other):
		return len(self.potential_teams) >= len(other.potential_teams)

	#def __eq__(self, other):
		#return self.getUID == other.getUID

	#def __ne__(self, other):
		#return self.getUID != other.getUID

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

	def getOverallExperience(self):
		return self.overallExperience

	def setOverallExperience(self, exp):
		self.overallExperience = exp
		return None

	def getCodeExperience(self):
		'''
		output -> dictionary mapping languages to integer rating of skill
		ex: dict = {'Python': 5 ... and so on}
		'''
		return self.codeExperience

	def setCodeExperience(self, tool, capability):
		'''
		input -> tool - string of a coding lanugage i.e.: 'Python'
			capability - string OR int that is integer rating of skill
		this function sets the student's particular language skill to a rating, casting the rating to an int as a safety measure
		'''
		self.codeExperience[tool] = capability
		return None

	def getAvailability(self):
		'''
		output -> dictionary representation of student's availability chart
			may want to add specifying parameters that narrow down for a certain day
		'''
		return self.availability

	def setAvailability(self, graph):
		'''
		input -> graph is an entire dictionary representing the student's entire weeklong availability
			#TODO build helper function that takes extra parameter of specific day and time slot, and adds that to a student's availability
		'''
		self.availability = graph
		return None

	def setTeammates(self, buddy):
		self.teammates.append(buddy)
		return None

	def getTeammates(self):
		return self.teammates

	# TODO figure out how criteria is represented


# -----------------------------------Sandbox Area -------------------------------------------------#
if __name__ == '__main__':
	student = Student('Brian', 'brian@brian.com')
	student.setCodeExperience('Python', 8)
	print(student.getCodeExperience())
	student.setOverallExperience(4)
	print('{} is this qualified: {}'.format(student.getName(), student.getOverallExperience()))

	# testing availability attributes
	print(student.getAvailability())
	student.setAvailability('Thursday', '12:00-2:00')
	print(student.getAvailability())
	student.setAvailability('Thursday', '2:00-4:00')
	print(student.getAvailability())

	# testing requested teammates list
	friend = Student('Jamie', 'jamie@yellow.edu')
	student.setTeammates(friend)
	for s in student.getTeammates():
		print(s)
	print(student)
