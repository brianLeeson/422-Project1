"""
Author(s): Brian Leeson + Jamie Zimmerman + Amie Corso

"""
import Team
import random
import copy
import itertools


class Classroom:

	def __init__(self, section, teacher):
		self.section = section  # 'W17', 'S17', etc.
		self.teacher = teacher  # 'Michal Young', etc.

		self.csv_file = ''  # the csv file containing all survey responses for this class
		self.studentList = []  # list of Student objects
		self.teamList = []  # list OFFICIAL list of Team objects (populated by sortIntoTeams())

		# These attributes are used during the sorting process (manage students)
		self.assignedStudents_viable = []
		self.assignedStudents_bad = []
		self.unassignedStudents = []

		# These attributes are used during the sorting process (manage teams)
		self.allViableTeams = []
		self.assignedTeams_viable = []
		self.assignedTeams_bad = []

		# TODO Is this how we want our weights to look?
		# We could break them out into individual attributes
		self.weights = []  # currently unused
		self.teamSize = 4

		self.sortingSuccess = False

	def __str__(self):
		return self.teacher + " " + str(self.section)

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
		Sorts the student class list (self.studentList) into teams of (self.teamSize) and populates
		member list self.officialTeamList with final selections.

		Calls:
		generateAllTeams()
		sortStudentList()
		getSeedTeams()
		attemptToPlace()
		....

		"""

		print("Student list is: ")
		for student in self.studentList:
			print(student.getName(), end=", ")
		print("\n")

		# Handle the case where the number of students is less than the teamSize,
		# and therefore there is only one possible team.
		if len(self.studentList) <= self.teamSize:
			the_team = Team.Team(1);
			for student in self.studentList:
				the_team.addMember(student)
				student.assignedTeam = the_team
			the_team.establish_metrics()
			if the_team.is_viable:
				self.assignedTeams_viable.append(the_team)
			else:
				self.assignedTeams_bad.append(the_team)
			self.teamList.append(the_team)

		else:
			#self.generateAllTeams()
			self.generateAllTeams_itertools()
			self.sortStudentList()
			self.getSeedTeams()
			self.attemptToPlace()
			self.handleUnassigned()
			for team in self.assignedTeams_viable:
				self.teamList.append(team)
			for team in self.assignedTeams_bad:
				self.teamList.append(Team)

		# Printed report to check results
		print("\n\nAfter running sortIntoTeams() : \n")

		print("Total number of students = ", len(self.studentList))
		print("assignedStudents_viable = ", end='')
		for student in self.assignedStudents_viable:
			print(student.name, end=", ")
		print()
		print("assignedStudents_bad = ", end='')
		for student in self.assignedStudents_bad:
			print(student.name, end=", ")
		print()
		print("unassigned_students = ", end='')
		for student in self.unassignedStudents:
			print(student.name, end=", ")
		print()

		print("Number of VIABLE (assigned) teams is: ", len(self.assignedTeams_viable))
		print("Number of UNVIABLE (assigned) teams is: ", len(self.assignedTeams_bad))

		print("\nReport of viable teams: ")
		for team in self.assignedTeams_viable:
			print("Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs,
				" time_overlap =", team.time_overlap, " viability =", team.is_viable)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		print("\nReport of UNviable teams: ")
		for team in self.assignedTeams_bad:
			print("Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs,
				  " time_overlap =",
				  team.time_overlap, " viability =", team.is_viable)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		return None

	def generateAllTeams(self):
		""" Populates member list allViableTeams with all viable teams of 3."""
		print("\n\nRUNNING GENERATE_ALL_TEAMS()\n")
		teamID = 0
		for s1 in self.studentList:
			for s2 in self.studentList:
				for s3 in self.studentList:
					if (s1 != s2 and s2 != s3 and s3 != s1):
						newteam = Team.Team(teamID)
						newteam.addMember(s1)
						newteam.addMember(s2)
						newteam.addMember(s3)
						newteam.establish_metrics()
						if newteam.is_viable:
							print("Team ", teamID, ": com_lang =", newteam.common_langs, " time_overlap =",
								  newteam.time_overlap, " viability =", newteam.is_viable)
							for member in newteam.member_list:
								print(member.name, end=' ')
							print()
							self.allViableTeams.append(newteam)
							# Giving each student a reference to the teams of which they are potentially a member.
							s1.potential_teams.append(newteam)
							s2.potential_teams.append(newteam)
							s3.potential_teams.append(newteam)
							teamID += 1

		self.allViableTeams.sort()
		self.allViableTeams.reverse()
		print()
		print("finished making teams")
		print("length of team list: ", len(self.allViableTeams))
		print()
		return None

	def generateAllTeams_itertools(self):
		""" Attempting version of generateAllTeams that uses Python's itertools module to create team combinations,
		which would allow us to implement variable teamsizes"""
		student_permutations = itertools.combinations(self.studentList, self.teamSize)

		teamID = 0
		for member_list in student_permutations:
			new_team = Team.Team(teamID)
			for student in member_list:
				new_team.addMember(student)
			new_team.establish_metrics()
			if new_team.is_viable:
				print("Team ", teamID, ": com_lang =", new_team.common_langs, " time_overlap =",
					  new_team.time_overlap, " viability =", new_team.is_viable)
				for member in new_team.member_list:
					member.potential_teams.append(new_team)
					print(member.name, end=' ')
				print()
				self.allViableTeams.append(new_team)
			teamID += 1

		self.allViableTeams.sort()
		self.allViableTeams.reverse()

		print()
		print("finished making teams")
		print("length of team list: ", len(self.allViableTeams))
		print()
		return None

	def sortStudentList(self):
		"""For each student in the studentList, sorts their list of potential teams in order of
		decreasing quality score.  Then sorts studentList in order of increasing number of potential teams.
		This is achieved by overwritten rich comparison methods.
		Returns None."""
		print("\n\nRUNNING SORT_STUDENT_LIST\n")
		for student in self.studentList:
			student.sort_potential_teams()
		# now sort our list of students by which has the fewest number of potential teams in their list
		self.studentList.sort()

		for student in self.studentList:
			print(student.getName(), ": len of potential teams = ", len(student.potential_teams))
			for team in student.potential_teams:
				print(team.quality_score, end=', ')

			print()

		return None

	def getSeedTeams(self):
		""" Generate the initial team list for further processing.
		Does not ensure validity of all teams."""
		print("\n\nRUNNING GET_SEED_TEAMS\n")

		for student in self.studentList:
			if student not in self.assignedStudents_viable:
				# here we try to find the best team for this unassigned student
				for team_to_consider in student.potential_teams:  # make sure we don't try to index out of the potential teams list
					this_one_works = True
					for student in team_to_consider.member_list:  # check each member of this team to make sure they are not already assigned
						if student in self.assignedStudents_viable:
							this_one_works = False

					if this_one_works:
						self.assignedTeams_viable.append(team_to_consider)
						for student in team_to_consider.member_list:
							student.assignedTeam = team_to_consider
							self.assignedStudents_viable.append(student)
						break  # out of the inner for loop, so we move on to the next student

		# generate the list of unassigned students
		for student in self.studentList:
			if student not in self.assignedStudents_viable:
				self.unassignedStudents.append(student)

		print("Total number of students is: ", len(self.studentList))
		print("Number of ASSIGNED students is: ", len(self.assignedStudents_viable))
		for student in self.assignedStudents_viable:
			print(student.name, end=", ")
		print()
		print("Number of UNASSIGNED students is: ", len(self.unassignedStudents))
		for student in self.unassignedStudents:
			print(student.name, end=", ")
		print()
		print("Note - we have not yet put these unassigned students on random teams.")

		for i in range(len(self.unassignedStudents)//self.teamSize): # number of complete teams we can make out of the unassigned students
			newID = 0
			newteam = Team.Team("unviable" + str(newID))
			for i in range(self.teamSize):
				newteam.addMember(self.unassignedStudents[0])
				self.unassignedStudents[0].assignedTeam = newteam
				self.assignedStudents_bad.append(self.unassignedStudents.pop(0))

			self.assignedTeams_bad.append(newteam)
			newteam.establish_metrics()
			newID += 1



		"""
		Now we have several items:
		assignedStudents_viable
		assignedStudents_bad
		unassignedStudents (which should have length studentList % teamSize)

		self.assignedTeams_viable
		self.assignedTeams_bad

		"""

		print("\n\nAfter randomly assigning the stragglers: ")
		print("length self.assignedStudents_viable = ", len(self.assignedStudents_viable))
		print("members: ", end='')
		for student in self.assignedStudents_viable:
			print(student.name, end=", ")
		print()
		print("length self.assignedStudents_bad = ", len(self.assignedStudents_bad))
		print("members: ", end='')
		for student in self.assignedStudents_bad:
			print(student.name, end=", ")
		print()
		print("length self.unassigned_students = ", len(self.unassignedStudents))
		print("members: ", end='')
		for student in self.unassignedStudents:
			print(student.name, end=", ")
		print()


		# TODO: deal with the unassigned leftover students
		return None

	def attemptToPlace(self):
		"""
		This function tries to assign students who are on unviable teams to viable ones via randomized hill-climbing approach.
		"""
		# choose a random student who's on a bad team
		# attempt to swap them with another random student (or should this be methodical?)
		# if the resulting (total) viability score is better
		# and at least one team is still viable, then keep the swap
		# otherwise, swap back and choose again
		print("\n\nRUNNING ATTEMPT_TO_PLACE...\n")
		print("but first, where we attttttt")
		print("Total number of students = ", len(self.studentList))
		print("assignedStudents_viable = ", end='')
		for student in self.assignedStudents_viable:
			print(student.name, end=", ")
		print()
		print("assignedStudents_bad = ", end='')
		for student in self.assignedStudents_bad:
			print(student.name, end=", ")
		print()
		print("unassigned_students = ", end='')
		for student in self.unassignedStudents:
			print(student.name, end=", ")
		print()

		print("Number of VIABLE (assigned) teams is: ", len(self.assignedTeams_viable))
		print("Number of UNVIABLE (assigned) teams is: ", len(self.assignedTeams_bad))

		print("\nReport of viable teams: ")
		for team in self.assignedTeams_viable:
			print("Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs, " time_overlap =",
				  team.time_overlap, " viability =", team.is_viable)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		print("\nReport of UNviable teams: ")
		for team in self.assignedTeams_bad:
			print("Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs,
				  " time_overlap =",
				  team.time_overlap, " viability =", team.is_viable)
			for member in team.member_list:
				print(member.name, end=' ')
			print()


		i = 0 # counter to ensure our while loop is not infinite
		while (len(self.assignedTeams_bad) > 0 and i < 100000): # note that this is potentially infinite
			bad_student_index = random.randint(0, len(self.assignedStudents_bad) - 1)
			swapee_index = random.randint(0, len(self.studentList) - 1)
			bad_student = self.assignedStudents_bad[bad_student_index]
			swapee = self.studentList[swapee_index]

			if swapee not in self.unassignedStudents:


				bad_team = bad_student.assignedTeam
				good_team = swapee.assignedTeam

				orig_total_quality = bad_team.quality_score + good_team.quality_score

				self.swapTwoStudents(bad_student, swapee)

				bad_team.establish_metrics()
				good_team.establish_metrics()
				new_total_quality = bad_team.quality_score + good_team.quality_score

				# case where both teams become viable - we want to keep this always
				if (bad_team.is_viable and good_team.is_viable):
					# make sure these teams and all their members are on the right lists
					self.place_good(bad_team)
					self.place_good(good_team)

				# case where at least one team is still viable and we want to keep the results
				elif (bad_team.is_viable) and (new_total_quality >= orig_total_quality):
					self.place_good(bad_team)
					self.place_bad(good_team)

				elif (good_team.is_viable) and (new_total_quality >= orig_total_quality):
					self.place_good(good_team)
					self.place_bad(bad_team)

				else: # case where we don't want to keep the results
					# swap the students back and nothing else should have to change
					self.swapTwoStudents(swapee, bad_student)
					# don't forget to recalculate the values for the respective teams
					bad_team.establish_metrics()
					good_team.establish_metrics()
				i += 1
			else:
				continue
		return None

	def handleUnassigned(self):
		""" Places any remaining unassigned students onto the best possible of the currently existing teams.
		IDEA:  Should the make sure that the unassigned students are the most available?"""

		print("RUNNING HANDLE_UNASSIGNED: ")
		while len(self.unassignedStudents) > 0:
			student = self.unassignedStudents[0]
			print("UNASSIGNED_STUDENT: ", student)
			possibleTeams = []
			for team in self.assignedTeams_viable: # we will only try to use previously viable teams to accommodate the unassigned students
				if len(team.member_list) < (self.teamSize + 1): # we don't want to include teams that already have an extra member
					original_team = team
					possible_team = copy.deepcopy(team) # this solved the problem of having multiple amies, but why?
					possible_team.addMember(student)
					possible_team.establish_metrics()
					possibleTeams.append([possible_team, original_team])

			best_team = possibleTeams[0][0]
			original_team = possibleTeams[0][1]
			for sublist in possibleTeams:
				potential_best = sublist[0]
				corresponding_original = sublist[1]
				if potential_best.quality_score > best_team.quality_score:
					best_team = potential_best
					original_team = corresponding_original
			# now we have the best team
			# get this student off of the unassigned list
			self.unassignedStudents.remove(student)
			# and put them (and the new team) on the correct list
			if best_team.is_viable: # if it's a viable team, we only need to update the unassigned student
				self.assignedTeams_viable.append(best_team)
				self.assignedStudents_viable.append(student)
			else: # otherwise, if the best we could do was create an unviable team, we should update everyone for reporting
				self.assignedTeams_bad.append(best_team)
				for member in best_team.member_list:
					if member not in self.assignedStudents_bad:
						self.assignedStudents_bad.append(member)
					if member in self.assignedStudents_viable:
						self.assignedStudents_viable.remove(member)

			# make sure every student has a reference to the new team they are on
			for member in best_team.member_list:
				member.assignedTeam = best_team

			# finally, remove the original 3-person team from its list
			self.assignedTeams_viable.remove(original_team)

		return None

	def place_good(self, team):
		"""
		Auxiliary func
		Make sure the team and all its members are on the "good" list and
		NOT on the "bad list.
		"""
		for student in team.member_list:
			if student not in self.assignedStudents_viable:
				self.assignedStudents_viable.append(student)
			if student in self.assignedStudents_bad:
				self.assignedStudents_bad.remove(student)

		if team not in self.assignedTeams_viable:
			self.assignedTeams_viable.append(team)
		if team in self.assignedTeams_bad:
			self.assignedTeams_bad.remove(team)
		return None

	def place_bad(self, team):
		"""
		Auxiliary func
		Make sure the team and all its members are on the "bad" list and
		NOT on the "good" list.
		"""
		for student in team.member_list:
			if student not in self.assignedStudents_bad:
				self.assignedStudents_bad.append(student)
			if student in self.assignedStudents_viable:
				self.assignedStudents_viable.remove(student)

		if team not in self.assignedTeams_bad:
			self.assignedTeams_bad.append(team)
		if team in self.assignedTeams_viable:
			self.assignedTeams_viable.remove(team)
		return None

	def swapTwoStudents(self, student1, student2):
		"""
		Auxiliary func
		swap the membership of student 1 with student 2
		"""

		student1.assignedTeam.member_list.remove(student1)
		student1.assignedTeam.member_list.append(student2)
		student2.assignedTeam.member_list.remove(student2)
		student2.assignedTeam.member_list.append(student1)
		tempteam = student1.assignedTeam
		student1.assignedTeam = student2.assignedTeam
		student2.assignedTeam = tempteam
		return None
# -------------------------------------------- Sandbox Area --------------------------------------#
if __name__ == '__main__':
	cs = Classroom('S17', 'Michal Young')
	students = [1, 2, 3, 'a', '4']
	cs.setStudentList(students)
	print(cs.classroomSize())
