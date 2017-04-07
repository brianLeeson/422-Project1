"""
Author(s): Brian Leeson

"""


class Classroom:

	def __init__(self):
		self._studentList = []
		self._groupList = []
		# TODO Is this how we want our weights to look?
		# We could break them out into individual attributes
		self.weights = []

	def getStudentList(self):
		return self._studentList

	def setStudentList(self, studentList):
		self._studentList = studentList
		return None

	def getGroupList(self):
		return self._groupList

	def setGroupList(self, groupList):
		self._groupList = groupList
		return None

	# TODO Getters and setters


