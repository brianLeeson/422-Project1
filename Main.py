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
- The key for the unviable teams is repeated..?
- teamsize bug - we can only handleUnassigned if we have enough teams.
 add logic to check for this.  IF we have to make a straggler garbage team, we could repeat "attemptToPlace()"
- TEST CASES!
- fix direct attribute reference with usage of getters and setters
    why isn't getName working with the __str__ override? (Student class)
- request consideration (up quality score?) (student.requests)
- useage of weights for sorting criteria
        How do we allow the user to populate the weights?
        Maybe we allow them to specify minimum acceptable skill in a language / minimum hours in common for a team.
        And then the weights are specified by the user ranking the relative importance of each criteria.
        What is our final decision on what it means to have a good team?
        i.e. What is the minimum viable overlap? Is this something that should be specifiable by user?

- Clean up printing

*IDEAS*:
What if we start by grabbing teams that have closer-to-average quality scores?
so that we don't make any unbreakable teams by the random swap method....

Handling the case of a student(s) who aren't viable on ANY teams... Or is this already taken care of by default?
(Do we want any special messages or handling?)

That weird bug where we lost a team......?



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
- cleaner, more descriptive comments/docstrings
- fix what Jamie manages to break

"""