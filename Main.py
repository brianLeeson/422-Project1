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

Need to increase random potential of swaps (including between members who are both on unviable teams).
So this means allowing swapees to be the entire pool of students not just assigned_viable

Add the logic to deal with unassigned students (groups not divisible by 3)
- what do we do if the class size is less than the teamsize?
- or if no viable teams can be created?  (maybe just report a message and abort the sort?)

- create some very small test cases, and intentionally unviable test cases



Handling the case of a student(s) who don't appear on ANY teams... Or is this already taken care of?

That weird bug where we lost a team......

fix direct attribute reference with usage of getters and setters
OR IS RALEIGH RIGHT AND THIS IS STUPID?

make sure student.teammates list gets populated once sort is over
OR DO WE EVEN NEED THIS?

TEST cases


Algorithm Wishlist:
- request consideration
- useage of weights for sorting criteria

Clean up printing for better discussion?


FOR MY COMRADES:
- should export wipe the original CSV file?  Because right now it's appending to it
- should multiple exports generate a new file?
- what other data can we report in the CSV?
- seems that the export isn't including 4th members
- what's going on with that error message printing around the language dictionaries?

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

