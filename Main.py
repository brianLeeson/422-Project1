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

Handling the case of a student(s) who aren't viable on ANY teams... Or is this already taken care of?

That weird bug where we lost a team......

fix direct attribute reference with usage of getters and setters
DO IT

Algorithm Wishlist:
- request consideration (up quality score) (student.requests)
- useage of weights for sorting criteria
- fix so that teamsize is a real parameter (itertools?)
Clean up printing for better discussion?

IDEAS:
What if we start by grabbing teams that have closer-to-average quality scores?
so that we don't make any unbreakable teams by the random swap method....

Student Class:
- I overwrote the CMP method because apparently you have to overwrite all 6 rich comparison operators
* why isn't getName working??

How do I get the __str__ override to print a prettier version? (for the Team class, for example)


BRIAN:
- teamSize parameter (keep/discard?)
- virtual environment?
- documentation


JAMIE:
- testing on multiple platforms
- unit tests?
- class so big that it breaks
- class with various multiples of teamsize (/not multiples)
- classes that CAN'T form teams
- classes that are smaller than teamsize
- does CSV for sure overwrite? (not append)
-
- what other data can we report in the CSV?
    for example:
        overlapping languages
        overlapped schedule (this would need be generated)
        quality score

- seems that the export isn't including team+1th members

AMIE:
-  algorithm notes above
- comments/docstrings
- fix what Jamie manages to break

"""