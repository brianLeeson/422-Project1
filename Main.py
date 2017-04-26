"""
Author(s): Amie Corso

"""
import Classroom
import fileProcess

ourclass = Classroom.Classroom("S17", "Michal Young")
ourclass.setCSV("fake_422_data.csv")
ourclass.setStudentList(fileProcess.process(ourclass.getCSV()))

for student in ourclass.studentList:
    print("Request list of: ", student, "= ", student.requests)

ourclass.sortIntoTeams()

"""Amie's Notes to herself:
TODO:
- fix direct attribute reference with usage of getters and setters
    why isn't getName working with the __str__ override? (Student class)
- Clean up printing
- Comments and such

*IDEAS*:
What if we start by grabbing teams that have median quality_scores, so that we don't create any unbreakable teams during the
randomization process?

What if we saved each iteration of the sorting process and grabbed the one that was overall best?

Other ideas:
Could we display a "sorting....." message on the GUI while the sort is in progress?
The output should display viability (or lackthereof) of the teams that were generated



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
        whether a team is viable or not
        the team+1th members

"""
