"""
Author(s): Brian Leeson

"""


class Classroom:

	def __init__(self):
		self._studentList = []
		self._groupList = []
		# TODO Is this how we want our weights to look?
		# We could break them out into individual attributes
		self._weights = []
		self._groupSize = 3

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
	# Note: imo weight should be set by setters, not at instantiation.

	def getGroupSize(self):
		return self._groupSize

	def setGroupSize(self, groupSize):
		self._groupSize = groupSize
		return None

	def sortIntoTeams(self):
		"""
		function sorts self._studentList into groups of self._groupSize
		based on an algorithm
		then sets that sorted list to self._groupList
		returns None
		"""
		# initial algorithm sorts first three into a group, then next three, etc.
		# TODO: Make algorithm better

		groupSize = self.getGroupSize()
		stList = self.getStudentList()[:]  # make copy of student list
		groupList = []

		while len(stList) > 0:
			# append first three members
			groupList.append(stList[:groupSize+1])
			# create new list minus first three members
			stList = stList[groupSize:]

		self.setGroupList(groupList)

		return None


