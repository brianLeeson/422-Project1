"""
Author(s): Amie Corso

"""
import Classroom
import fileProcess

ourclass = Classroom.Classroom("S17", "Michal Young")
ourclass.setCSV("fake_422_data.csv")
ourclass.setStudentList(fileProcess.process(ourclass.getCSV()))

#for student in ourclass.studentList:
#    print(student.name, ": ", student.availability)


ourclass.sortIntoTeams()


"""Amie's Notes to herself:

TODO:
Make sure that the population of the "teamList" also includes wiping it if it had anything in it beforehand...
So that if we get to the point where we are re-doing sorts, we don't end up with multiples of the classsize.


Need to increase random potential of swaps (including between members who are both on unviable teams).
So this means allowing swapees to be the entire pool of students not just assigned_viable

Add the logic to deal with unassigned students (groups not divisible by 3)

Handling the case of a student(s) who don't appear on ANY teams...

That weird bug where we lost a team......

fix direct attribute reference with usage of getters and setters

make sure student.teammates list gets populated once sort is over

TEST cases


Algorithm Wishlist:
- request consideration
- useage of weights for sorting criteria

Clean up printing for better discussion?



IDEAS:
if we fail to accommodate every student, we repeat the process starting with a different FIRST team assignment?
Everything else stays the same... it just creates more opportunity for new seeds?

What if we start by grabbing teams that have closer-to-average quality scores?
so that we don't make any unbreakable teams by the random swap method....

Student Class:
- I overwrote the CMP method because apparently you have to overwrite all 6 rich comparison operators
* why isn't getName working??

How do I get the __str__ override to print a prettier version? (for the Team class, for example)
"""



