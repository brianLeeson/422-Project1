import Student
import Team
import Classroom
import fileProcess
import random
import string

ourclass = Classroom.Classroom("S17", "Michal Young")
ourclass.setCSV("fake_422_data.csv")
ourclass.setStudentList(fileProcess.process(ourclass.getCSV()))

ourclass.sortIntoTeams()

# need to increase random potential of swaps (including between members who are both on unviable teams)
# so we should be able to swap between any two students who are on the studentList
# and add logic to deal with whatever result

# clean up printing for better discussion

# add logic to deal with unassigned students (groups not divisible by 3)



