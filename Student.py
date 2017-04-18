"""
Author(s): Brian Leeson + Jamie Zimmerman

"""
import datetime


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	# NOTE: I think that any attribute of Student that could be a list should be a tuple.
	# There might be some aliasing issues we could nip in the bud if we chose tuples

	def __init__(self, name, email):
		self.UID = 0  # TODO implement UID as a UUID? *Can't* be student ID. FERPA
		self.name = name
		self.email = email

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

	def __str__(self):
		# TODO fix this usage - throws a type error because it can't print int type (from UID)
		# example, when you call print(student)
		return self.getName()

	def __cmp__(self, other):
		return self.getUID() == other.getUID()

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
		return None

	def getUID(self):
		return self.UID

	def setUID(self, UID):
		self.UID = UID
		return None

	def getOverallExperience(self):
		return self.overallExperience

	def setOverallExperience(self, exp):
		self.overallExperience = exp
		return None

	def getCodeExperience(self):
		return self.codeExperience

	def setCodeExperience(self, tool, capability):
		self.codeExperience[tool] = capability
		return None

	def getAvailability(self):
		'''
		output -> dictionary representation of student's availability chart
			may want to add specifying parameters that narrow down for a certain day
		'''
		return self.availability

	def setAvailability(self, graph):
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
