"""
Author(s): Jamie Zimmerman + Amie Corso

class Team:
Team objects contain collections of Student objects.
Team attributes are used to keep track of members, as well as store information about the quality and viability of the team.
Methods calculate and populate these attributes based on the characterists of the member Student objects.
Note overwritten rich comparison methods.
"""

from Student import Student  # from the module, import the class


class Team:

	def __init__(self, identifier):
		self.number = identifier
		self.member_list = []
		self.team_name = '' # Not currently used

		self.num_common_langs = 0
		self.common_langs = []
		self.time_overlap = 0

		self.quality_score = 0
		self.is_viable = False

	def __str__(self):
		return self.number

	def __lt__(self, other):
		return self.quality_score < other.quality_score

	def __le__(self, other):
		return self.quality_score <= other.quality_score

	def __gt__(self, other):
		return self.quality_score > other.quality_score

	def __ge__(self, other):
		return self.quality_score >= other.quality_score

	def __eq__(self, other):
		return self.number == other.number

	def __ne__(self, other):
		return self.number != other.number

	def calc_common_lang(self):
		""" Compares language overlap among team members.
		Populates member list of common languages (self.common_langs).
		Sets member variable num_common_langs.
		A language is considered overlapping if all members have a self-reported proficiency of at least 3.
		Called by establish_metrics().
		"""
		self.common_langs = []  # RESET the language list in case we are updating a pre-calculated team
		languagelist = ['Python', 'Java', 'Javascript', 'C', 'C++', 'PHP', 'HTML', 'SQL', 'Bash/Unix']
		for language in languagelist:
			speakers = 0
			for student in self.member_list:
				if student.getCodeExperience()[language] >= 3: # ARBITRARY (parameterize?)
					speakers += 1
			if speakers == 3:
				self.common_langs.append(language)
		self.num_common_langs = len(self.common_langs)
		return None

	def calc_time_overlap(self):
		""" Compares schedules among team members.
		Calculates total time overlaps and sets self.time_overlap, the number of overlapping timeslots among teammembers.
		A timeslot is considered overlapping if all members of the team have indicated availability. Called by establish_metrics().
		"""
		overlap = 0
		dayslist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
		for day in dayslist:
			member_avails = [] # collect sublists: each member's availability list for a given day
			for student in self.member_list:
				member_avails.append(student.getAvailability()[day])

			for i in range(len(member_avails[0])): # For each time slot
				overlapping = True
				for j in range(len(member_avails)): # for each student
					if (member_avails[j][i] == 0): # if any entry in that slot == 0, we do not consider it mutually available
						overlapping = False
				if overlapping:
					overlap += 1
		self.time_overlap = overlap
		return None

	def calc_viability(self):
		""" Determines whether team meets minimum viability requirements.
		Sets member variable is_viable to True/False accordingly. Called by establish_metrics()."""
		self.is_viable = False  # RESET in case we were re-calculating a pre-existing team
		if self.num_common_langs >= 1: # ARBITRARY (parameterize?)
			if self.time_overlap >= 3: # ARBITRARY (parameterize?)
				self.is_viable = True
		return None

	def calc_quality_score(self):
		""" Calculates overall quality score based on schedule overlap, language overlap.
		Returns integer score value.  Called by establish_metrics()."""

		# note that prototype weighs time_overlap by factor of 2.  Does not currently include weighting of requests.
		# This is arbitrary and should be determined for final MVP, or parameterize for user by input.
		self.quality_score = self.time_overlap + 2*self.num_common_langs
		return None

	def establish_metrics(self):
		"""Wrapper function for setting up new team.
		Calculates and populates member variables:
		self.num_common_langs
		self.common_langs
		self.time_overlap
		self.quality_score
		self.is_viable"""
		self.calc_common_lang()
		self.calc_time_overlap()
		self.calc_viability()
		self.calc_quality_score()
		return None

	def getNumber(self):
		return self.number

	def setNumber(self, num):
		self.number = num
		return None
	
	def getMemberList(self):
		return self.member_list

	def setMemberList(self, grouping):
		self.member_list = grouping
		return None

	def addMember(self, teammate):
		self.member_list.append(teammate)
		return None
	
	def getTeamName(self):
		return self.team_name

	def setTeamName(self, team_name):
		self.team_name = team_name
		return None

# -------------------------------------------- Sandbox Area --------------------------------------#
if __name__ == '__main__':
	team = Team(6)
	student1 = Student('brian', 'brian@brian.com')
	student2 = Student('jamie', 'jamie@yellow.com')
	student3 = Student('amie', 'amie@red.edu')
	team.setMemberList([student1, student2, student3])
	for guy in team.getMemberList():
		print(guy)
	team.addMember(student1)
	for guy in team.getMemberList():
		print(guy)
