"""
Author(s): Brian Leeson + Jamie Zimmerman

"""


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	# NOTE: I think that any attribute of Student that could be a list should be a tuple.
	# There might be some aliasing issues we could nip in the bud if we chose tuples

	def __init__(self, name, email, criteria):
		self.UID = 0  # TODO implement UID as a UUID? *Can't* be student ID. FERPA
		self.name = name
		self.email = email
		self.criteria = criteria
		
		self.overallExperience = 0 #overall experience score - how many upper div CS classes completed
		self.codeExperience = {'Python': 0,
					'Java': 0,
					'JavaScript': 0,
					'C': 0,
					'C++': 0}

	def __str__(self):
		return self.getName() + " " + self.getUID()

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
	# TODO figure out how criteria is represented


#-----------------------------------Sandbox Area -------------------------------------------------#
if __name__ == '__main__':
	student = Student('Brian', 'brian@brian.com', 5)
	student.setCodeExperience('Python', 8)
	print(student.getCodeExperience())
	student.setOverallExperience(4)
	print('{} is this qualified: {}'.format(student.getName(), student.getOverallExperience()))
