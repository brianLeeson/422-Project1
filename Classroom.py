"""
Author(s): Brian Leeson + Jamie Zimmerman + Amie Corso

class Classroom:
A Classroom object is instantiated upon import of a CSV file containing survey data.
Contains list of Student objects, representing the students in the class, and list of Team objects, representing
the final teams.
Contains umbrella sorting method "sortIntoTeams()" and all necessary auxiliary functions for creating teams out of
the student data.  Called when "Sort" button is pressed in the GUI.
"""
import Team
import random
import itertools


class Classroom:
	def __init__(self, section, teacher):
		self.section = section  # 'W17', 'S17', etc.
		self.teacher = teacher  # 'Michal Young', etc.

		self.csv_file = ''  # the CSV file containing all survey responses for this class
		self.studentList = []  # list of Student objects, populated upon import of CSV
		self.teamList = []  # list OFFICIAL list of Team objects (populated by sortIntoTeams())

		# These attributes are used during the sorting process (manage students)
		self.assignedStudents_viable = []
		self.assignedStudents_bad = []
		self.unassignedStudents = []

		# These attributes are used during the sorting process (manage teams)
		self.allViableTeams = []
		self.assignedTeams_viable = []
		self.assignedTeams_bad = []
		self.uniqueID = 0  # used to create unique identifiers throughout team creation/destruction process

		# self.weights = []  # currently unused, instead these parameters are specified individually below
		self.teamSize = 3  # 3 by default

		self.sortingSuccess = False

		# Arbitrary attributes for defining team viability and quality.
		# Parameterized to allow easy adjustment, and potentially input from the user in the future.
		self.min_acceptable_lang_proficiency = 3  # self-reported proficiency of (min_acceptable_lang_proficiency)\
		#  (scale of 1 -5) or greater means language could be used
		self.min_team_overlapping_langs = 1  # teams need at least (min_team_overlapping_langs) language in common
		self.min_team_overlapping_timeslots = 2  # at least (2 * min_team_overlapping_timeslots) mutual hours per week necessary
		self.schedule_factor = 1  # (schedule_factor * team.num_overlapping_timeslots) is added to team quality score
		self.langs_factor = 2  # (langs_factor * team.num_overlapping_langs) is added to quality score
		self.request_factor = 1  # adds (request_factor) to quality_score of team for each request that is satisfied

	# (for each instance that a duckID in a team member's request list is that of an actual teammate)

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
		Returns None.

		Calls:
		performSort()

		"""
		print("Student list is: ")
		for student in self.studentList:
			print(student.getName(), end=", ")
		print("\n")

		# Handle the case where the number of students is less than the teamSize,
		# and therefore there is only one possible team.
		if len(self.studentList) <= self.teamSize:
			the_team = Team.Team(1)
			for student in self.studentList:
				the_team.addMember(student)
				student.assignedTeam = the_team
			the_team.establish_metrics(
										self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
										self.min_team_overlapping_timeslots, self.schedule_factor, self.langs_factor,
										self.request_factor
										)
			if the_team.is_viable:
				self.assignedTeams_viable.append(the_team)
			else:
				self.assignedTeams_bad.append(the_team)

		else:
			max_sort_attempts = 5  # maximum times that we will try to run sorting algorithm
			current_attempt = 0
			while current_attempt < max_sort_attempts:
				print("\n SORT ATTEMPT", str(current_attempt))
				self.performSort()  # wrapper function for all sorting subfunctions
				if len(self.assignedTeams_bad) > 0:  # if we still have unviable teams...
					current_attempt += 1  # try again
				else:  # otherwise, short-circuit the while loop
					current_attempt = max_sort_attempts

		# finally, populate final team list with results
		for team in self.assignedTeams_viable:
			self.teamList.append(team)
		for team in self.assignedTeams_bad:
			self.teamList.append(team)
		return None

	def performSort(self):
		# first reset member attributes, in case this is not the first sort we are performing
		self.assignedStudents_viable = []
		self.assignedStudents_bad = []
		self.unassignedStudents = []
		self.allViableTeams = []
		self.assignedTeams_viable = []
		self.assignedTeams_bad = []
		self.uniqueID = 0

		self.generateAllTeams_itertools()
		self.sortStudentList()
		self.getSeedTeams()
		if len(
				self.unassignedStudents) > 0:  # only execute the following if our class size is not a multiple of teamSize
			self.handleUnassigned()
		self.attemptToPlace()  # attempt to refine the assignments after unassigned students have been assigned to team(s).
		return None

	def generateAllTeams_itertools(self):
		""" Uses Python's itertools module to generate all possible team combinations of size teamSize.
		Establishes team metrics and assesses viability of each team, appending all viable teams to
		self.allViableTeams.  Returns None."""

		student_permutations = itertools.combinations(self.studentList, self.teamSize)
		for member_list in student_permutations:
			new_team = Team.Team(self.uniqueID)
			for student in member_list:
				new_team.addMember(student)
			new_team.establish_metrics(
										self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
										self.min_team_overlapping_timeslots, self.schedule_factor, self.langs_factor,
										self.request_factor
										)
			if new_team.is_viable:
				for member in new_team.member_list:
					member.potential_teams.append(new_team)
				self.allViableTeams.append(new_team)
			self.uniqueID += 1  # increment class variable uniqueID any time it is used

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
		This is achieved by overwritten rich comparison methods.  Returns None."""

		# print("\n\nRUNNING SORT_STUDENT_LIST\n")
		for student in self.studentList:
			student.sort_potential_teams()
		# now sort our list of students by which has the fewest number of potential teams in their list
		self.studentList.sort()

		return None

	def getSeedTeams(self):
		""" Generate the initial team list for further processing.
		Does not ensure validity of all teams."""
		print("\n\nRUNNING GET_SEED_TEAMS\n")

		for student in self.studentList:
			if student not in self.assignedStudents_viable:
				# here we try to find the best team for this unassigned student
				# make sure we don't try to index out of the potential teams list
				for team_to_consider in student.potential_teams:
					this_one_works = True
					# check each member of this team to make sure they are not already assigned
					for student in team_to_consider.member_list:
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

		for i in range(len(
				self.unassignedStudents) // self.teamSize):  # number of complete teams we can make out of the unassigned students
			newteam = Team.Team(self.uniqueID)
			self.uniqueID += 1  # increment to maintain uniqueness of IDs
			for i in range(self.teamSize):
				newteam.addMember(self.unassignedStudents[0])
				self.unassignedStudents[0].assignedTeam = newteam
				self.assignedStudents_bad.append(self.unassignedStudents.pop(0))

			self.assignedTeams_bad.append(newteam)
			newteam.establish_metrics(
										self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
										self.min_team_overlapping_timeslots, self.schedule_factor, self.langs_factor,
										self.request_factor
										)

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
		return None

	def attemptToPlace(self):
		"""
		This function tries to assign students who are on unviable teams to viable ones via randomized hill-climbing approach.
		Chooses a random student who is on a bad team and attempts to swap them with another random student.
		Keeps the result of the swap only if a previously unviable team was made viable, or if at least one team remains viable
		and the overall quality score (sum of both teams considered) increases.
		"""
		print("\n\nRUNNING ATTEMPT_TO_PLACE...\n")
		print("but first, what do things look like?:")
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
			print(
					"Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs,
					" time_overlap =",
					team.time_overlap, " viability =", team.is_viable
					)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		print("\nReport of UNviable teams: ")
		for team in self.assignedTeams_bad:
			print(
					"Team ", team.number, "Quality score: ", team.quality_score, ": com_lang =", team.common_langs,
					" time_overlap =",
					team.time_overlap, " viability =", team.is_viable
					)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		i = 0  # counter to ensure our while loop is not infinite
		# We can stop when all teams are viable or we've performed this enough times
		while (len(self.assignedTeams_bad) > 0 and i < 20000):
			bad_student_index = random.randint(0, len(self.assignedStudents_bad) - 1)
			swapee_index = random.randint(0, len(self.studentList) - 1)
			bad_student = self.assignedStudents_bad[bad_student_index]
			swapee = self.studentList[swapee_index]

			if swapee not in self.unassignedStudents:  # self.unassignedStudents should actually be empty at this point anyway
				bad_team = bad_student.assignedTeam
				good_team = swapee.assignedTeam

				orig_total_quality = bad_team.quality_score + good_team.quality_score

				self.swapTwoStudents(bad_student, swapee)

				bad_team.establish_metrics(
											self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
											self.min_team_overlapping_timeslots, self.schedule_factor, self.langs_factor,
											self.request_factor
											)
				good_team.establish_metrics(
											self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
											self.min_team_overlapping_timeslots, self.schedule_factor,
											self.langs_factor, self.request_factor
											)
				new_total_quality = bad_team.quality_score + good_team.quality_score

				# case where both teams become viable - we want to keep this always
				if (bad_team.is_viable and good_team.is_viable):
					# make sure these teams and all their members are on the right lists
					self.place_good(bad_team)
					self.place_good(good_team)

				# case where at least one team is still viable and we want to keep the results
				elif bad_team.is_viable and (new_total_quality >= orig_total_quality):
					self.place_good(bad_team)
					if good_team.is_viable:
						self.place_good(good_team)
					else:
						self.place_bad(good_team)

				elif good_team.is_viable and (new_total_quality >= orig_total_quality):
					self.place_good(good_team)
					if bad_team.is_viable:
						self.place_good(bad_team)
					else:
						self.place_bad(bad_team)

				else:  # case where we don't want to keep the results
					# swap the students back and nothing else should have to change
					self.swapTwoStudents(swapee, bad_student)
					# don't forget to recalculate the values for the respective teams
					bad_team.establish_metrics(
												self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
												self.min_team_overlapping_timeslots, self.schedule_factor,
												self.langs_factor, self.request_factor
												)

					good_team.establish_metrics(
												self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
												self.min_team_overlapping_timeslots, self.schedule_factor,
												self.langs_factor, self.request_factor
												)
				i += 1
			else:
				continue

		print("\n And now what have we got?....\n")
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
			print(
					"Team ", team.number, "Quality score: ", team.quality_score,
					": com_lang =", team.common_langs, " time_overlap =",
					team.time_overlap, " viability =", team.is_viable
					)
			for member in team.member_list:
				print(member.name, end=' ')
			print()

		print("\nReport of UNviable teams: ")
		for team in self.assignedTeams_bad:
			print(
				"Team ", team.number, "Quality score: ", team.quality_score,
				": com_lang =", team.common_langs, " time_overlap =",
				team.time_overlap, " viability =", team.is_viable
					)
			for member in team.member_list:
				print(member.name, end=' ')
			print()
		return None

	def handleUnassigned(self):
		""" Places any remaining unassigned students onto the best possible of the currently existing teams.
		Does not allow teams to have more than teamSize + 1 members.

		NOTE: the following not yet implemented:
		If there are not enough teams to accommodate all unassigned students, no placement occurs and a team is simply created
		from the unassigned students.  AttemptToPlace() is called again to attempt to optimize this random team. Returns None.
		"""

		print("\nRUNNING HANDLE_UNASSIGNED: ")
		# Case where we have enough teams to accommodate all unassigned students.
		if len(self.unassignedStudents) <= (len(self.assignedTeams_viable) + len(self.assignedTeams_bad)):

			while len(self.unassignedStudents) > 0:  # while we still have students waiting to be assigned
				student = self.unassignedStudents[0]  # grab the first one sitting in the list
				print("processing UNASSIGNED_STUDENT: ", student)
				possibleTeams = []
				for i in range(len(self.assignedTeams_viable)):  # we will generate possible teams from existing teams
					original_team = self.assignedTeams_viable[i]
					if len(original_team.member_list) < (
						self.teamSize + 1):  # we don't want to include teams that already have an extra member
						possible_team = Team.Team(
							self.uniqueID)  # copy the team so we can modify it without destroying original
						self.uniqueID += 1
						for member in original_team.member_list:
							possible_team.addMember(member)
						possible_team.addMember(student)
						possible_team.establish_metrics(
														self.min_acceptable_lang_proficiency,
														self.min_team_overlapping_langs,
														self.min_team_overlapping_timeslots, self.schedule_factor,
														self.langs_factor, self.request_factor
															)
						# populating a structure that associates the possible new team and the original team from which it was derived
						possibleTeams.append([possible_team, original_team])

				# REPEATING IDENTICAL PROCESS for the teams in the unviable list.
				for i in range(len(self.assignedTeams_bad)):
					original_team = self.assignedTeams_bad[i]
					if len(original_team.member_list) < (self.teamSize + 1):
						possible_team = Team.Team(self.uniqueID)
						self.uniqueID += 1
						for member in original_team.member_list:
							possible_team.addMember(member)
						possible_team.addMember(student)
						possible_team.establish_metrics(
														self.min_acceptable_lang_proficiency,
														self.min_team_overlapping_langs,
														self.min_team_overlapping_timeslots, self.schedule_factor,
														self.langs_factor, self.request_factor
														)
						possibleTeams.append([possible_team, original_team])

				best_team = possibleTeams[0][0]  # initialize best_team to be first team to consider
				original_team = possibleTeams[0][1]  # initialize original_team to be corresponding original team
				for sublist in possibleTeams:  # examine each possible team to find the best one
					potential_best = sublist[0]
					corresponding_original = sublist[1]
					if potential_best.quality_score > best_team.quality_score:
						best_team = potential_best
						original_team = corresponding_original
				# now we have the best team for this unassigned student, and a reference to the original version of this team
				# place this best team and its members in the correct data structures
				if best_team.is_viable:
					self.place_good(best_team)
				else:
					self.place_bad(best_team)

				# Get the original team off of whatever list it was on
				if original_team in self.assignedTeams_viable:
					self.assignedTeams_viable.remove(original_team)
				else:
					if original_team in self.assignedTeams_bad:
						self.assignedTeams_bad.remove(original_team)

				# make sure every student has a reference to the new team they are on
				for member in best_team.member_list:
					member.assignedTeam = best_team

		# The case where we don't have enough teams to accommodate all unassigned students....
		# We simply make a team out of the unassigned students, and make one more call to attemptToPlace() to optimize
		# this random team.
		else:
			newteam = Team.Team(self.uniqueID)
			self.uniqueID += 1
			for student in self.unassignedStudents:
				newteam.addMember(student)
				student.assignedTeam = newteam
			newteam.establish_metrics(
										self.min_acceptable_lang_proficiency, self.min_team_overlapping_langs,
										self.min_team_overlapping_timeslots, self.schedule_factor, self.langs_factor,
										self.request_factor
										)
			if newteam.is_viable:
				self.place_good(newteam)
			else:  # newteam is not viable
				self.place_bad(newteam)
		return None

	def place_good(self, team):
		"""
		Auxiliary function used for correctly categorizing teams (and their student objects) that may have changed members or status.
		Make sure the team and all its members are on the "good" list and
		are NOT on the "bad" list.
		"""
		for student in team.member_list:
			if student not in self.assignedStudents_viable:
				self.assignedStudents_viable.append(student)
			if student in self.assignedStudents_bad:
				self.assignedStudents_bad.remove(student)
			if student in self.unassignedStudents:
				self.unassignedStudents.remove(student)

		if team not in self.assignedTeams_viable:
			self.assignedTeams_viable.append(team)
		if team in self.assignedTeams_bad:
			self.assignedTeams_bad.remove(team)
		return None

	def place_bad(self, team):
		"""
		Auxiliary function used for correctly categorizing teams (and their student objects) that may have changed members or status.
		Makes sure the team and all its members are on the "bad" list and
		are NOT on the "good" list.
		"""
		for student in team.member_list:
			if student not in self.assignedStudents_bad:
				self.assignedStudents_bad.append(student)
			if student in self.assignedStudents_viable:
				self.assignedStudents_viable.remove(student)
			if student in self.unassignedStudents:
				self.unassignedStudents.remove(student)

		if team not in self.assignedTeams_bad:
			self.assignedTeams_bad.append(team)
		if team in self.assignedTeams_viable:
			self.assignedTeams_viable.remove(team)
		return None

	def swapTwoStudents(self, student1, student2):
		"""
		Auxiliary function, called by attemptToPlace().
		Swaps the team membership of student1 and student2.
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
	team = Team.Team(6)
