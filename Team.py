"""
Author(s): Jamie Zimmerman

"""

from Student import Student #from the module, import the class

class Team:

	def __init__(self, identifier):
		self.number = identifier #TODO make this a UID
		self.member_list = []
		self.team_name = ''
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
		if len(self.member_list) == 3:
			return "can't have over 3 people" #TODO error checking - how does user become informed if it has tried to add too many people
		self.member_list.append(teammate)
		return None
	
	def getTeamName(self):
		return self.team_name
	def setTeamName(self, team_name):
		self.team_name = team_name
		return None	

#-------------------------------------------- Sandbox Area --------------------------------------#
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
	
