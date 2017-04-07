class StudentSummary:
	""" 
	This class will represent an individuals survey results
	"""

	def __init__(self, name, criteria):
		self._name = name
		# implement UID as a UUID? *Can't* be student ID. FERPA
		self._UID = 0  # TODO
		self._criteria = criteria

	def __str__(self):
		return self.getName()

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

