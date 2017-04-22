"""
Author(s): Jamie Zimmerman + Amie Corso

"""

from Student import Student  # from the module, import the class


class Team:

	def __init__(self, identifier):
		self.number = identifier
		self.member_list = []
		self.team_name = ''

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
		""" Compare language overlap among team members.
		Populates member list of common languages (self.common_langs).
		Sets member variable num_common_langs."""
		self.common_langs = []  # RESET the language list in case we are updating an pre-calculated team
		languagelist = ['Python', 'Java', 'Javascript', 'C', 'C++', 'PHP', 'HTML', 'SQL', 'Bash/Unix']
		for language in languagelist:
			speakers = 0
			for student in self.member_list:
				if student.getCodeExperience()[language] >= 3:
					speakers += 1
			if speakers == 3:
				self.common_langs.append(language)
		self.num_common_langs = len(self.common_langs)
		return None

	def calc_time_overlap(self):
		""" Compare schedules among team members.
		Calculates total time overlaps and sets self.time_overlap."""
		overlap = 0
		dayslist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
		# TODO: below 3 lines hardcodes team size 3
		s1 = self.member_list[0]
		s2 = self.member_list[1]
		s3 = self.member_list[2]
		for day in dayslist:
			s1_avail = s1.getAvailability()[day]
			s2_avail = s2.getAvailability()[day]
			s3_avail = s3.getAvailability()[day]

			for i in range(len(s1_avail)):
				if (s1_avail[i] == 1) and (s2_avail[i] == 1) and (s3_avail[i] == 1):
					overlap += 1

		self.time_overlap = overlap
		return None

	def calc_viability(self):
		""" Determines whether team meets minimum viability requirements.
		and returns True / False accordingly."""
		self.is_viable = False  # RESET in case we were re-calculating a pre-existing team
		if self.num_common_langs >= 1:
			if self.time_overlap >= 4:
				self.is_viable = True
		return None

	def calc_quality_score(self):
		""" Calculates overall quality score based on schedule overlap, language overlap.
		Returns integer score value."""

		# note that prototype weighs time_overlap by factor of 2
		self.quality_score = self.time_overlap + 2*self.num_common_langs
		return None

	def establish_metrics(self):
		"""Wrapper function for setting up new team."""
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
		#if len(self.member_list) == 3:  # TODO don't hard code 3, compare to group size
			#return False  # TODO error checking - how does user become informed if it has tried to add too many people
							# Or should we handle this case elsewhere in the function(s) that may use addMember?
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
