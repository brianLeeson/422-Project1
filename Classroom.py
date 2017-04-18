"""
Author(s): Brian Leeson + Jamie Zimmerman

"""

from Team import Team


class Classroom:

	def __init__(self, section, teacher):
		self.section = section  # 'W17', 'S17', etc.
		self.teacher = teacher  # 'Michal Young', etc.
		
		self.csv_file = ''  # the csv file containing all survey responses for this class
		self.studentList = []  # list of Student objects
		self.teamList = []  # this is assumed ot be the final sorted team list

		# TODO Is this how we want our weights to look?
		# We could break them out into individual attributes
		self.weights = []
		self.teamSize = 3

		self.sortingSuccess = False
				
	def getSection(self):
		return self.section

	def setSection(self, section):
		self.section = section
		return None

	def getTeacher(self):
		return self.teacher

	def setTeacher(self, teacher):
		self.teacher = teacher
		return None

	def getCSV(self):
		return self.csv_file

	def setCSV(self, csv_file):
		self.csv_file = csv_file
		return None

	def getStudentList(self):
		return self.studentList

	def setStudentList(self, studentList):
		self.studentList = studentList
		return None

	def classroomSize(self):
		return len(self.studentList)

	def getTeamList(self):
		return self.teamList

	def setTeamList(self, teamList):
		self.teamList = teamList
		return None

	def getTeamSize(self):
		return self.teamSize

	def setTeamSize(self, teamSize):
		self.teamSize = teamSize
		return None

	def sortIntoTeams(self):
		"""
		function sorts self._studentList into groups of self._teamSize
		based on an algorithm
		then sets that sorted list to self.teamList
		returns None
		"""
		# initial algorithm sorts first three into a group, then next three, etc.
		# TODO: Make algorithm better.
		# TODO: can scrap everything, so long as self.teamList is [teamObj, teamObj, teamObj...]

		teamSize = self.getTeamSize()
		stList = self.getStudentList()[:]  # make copy of student list
		teamList = []
		teamUID = 0
		while len(stList) > 0:
			t = Team(teamUID)
			for student in stList[:teamSize+1]:
				t.addMember(student)

			# append first three members
			teamList.append(t)

			# create new list minus first three members
			stList = stList[teamSize:]

			teamUID += 1

		self.setTeamList(teamList)

		return None

# -------------------------------------------- Sandbox Area --------------------------------------#
if __name__ == '__main__':
	cs = Classroom('S17', 'Michal Young')
	students = [1, 2, 3, 'a', '4']
	cs.setStudentList(students)
	print(cs.classroomSize())
