class StudentSummary:
	""" 
	
	"""

	def __init__(self, name, UID, criteria):
		"""
		This function will represent an individuals survey results
		:param name: student name
		:param UID: UUID. *Can't* be student ID. FERPA
		:param criteria: a list of values? individual arguments?
		"""
		self._name = name
		self._UID = UID
		self._criteria = criteria

	def __str__(self):
		return self.getName()

	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name
		return None

