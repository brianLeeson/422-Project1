"""
Author(s): Brian Leeson

"""


class Student:
	""" 
	This class will represent an individuals survey results
	"""

	# NOTE: I think that any attribute of Student that could be a list should be a tuple.
	# There might be some aliasing issues we could nip in the bud if we chose tuples

	def __init__(self, name, email, criteria):
		self._UID = 0  # TODO implement UID as a UUID? *Can't* be student ID. FERPA
		self._name = name
		self._email = email
		self._criteria = criteria

	def __str__(self):
		return self.getName() + " " + self.getUID()

	def __cmp__(self, other):
		return self.getUID() == other.getUID()

	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name
		return None

	def getUID(self):
		return self. _UID

	def setUID(self, UID):
		self._UID = UID
		return None

	# TODO figure out how criteria is represented

