#test_cases/

This folder contains various sample inputs meant to test the robustness of the sorting algorithm.

generate.py -> this script writes the csv files. It creates random strings for names, random numbers for coding skills, and chooses randomly from a list of time availability combinations. This script should not be used any more, as it has already created the below sample class inputs.

no_pairings_extreme.csv -> a classroom where every student has literally NO time availability, has listed "None" for every one of their meeting times. This situation is wildly unrealistic to happen in real-life.
	RESULTS: PASSED. The program did make teams and export the results. Most teams had a zero quality score, but the program did determine quality scores where overlapping programming language experience counted. time < 10 seconds.

no_pairings.csv -> a classroom where very few people have any meeting times, i.e. most people can only meet once per week.
	RESULTS: PASSED. simiarly to the extreme case, most teams had a quality score of zero, HOWEVER, the algorithm determined a team with quality score of 7, ostensibly for overlapping time. Given a scenario where collectively each student's meeting time is less restrictive, there are more teams with a decent score and very few teams of garbage pairings. time <10 seconds.

odd_one_out.csv -> When team sizes are only 3, and there are 4 students in the class. This should create one team of 4.
	RESULTS: ********FAILED. in Classroom.py line 462, index error.

one_extra.csv -> The number of students in the class is a multiple of 3 + 1 more student. So this should create only one team of 4.
	RESULT: PASSED. created two teams of 3 and one team of 4. time < 3 seconds.

two_extra.csv -> The number of students in the class is a multiple of 3 + 2 more students. So this should create two teams of 4.
	RESULTS: PASSED. program creates 3 groups of 3 and 2 groups of 4. time < 5 seconds.

too_big.csv -> Tests the upper limit on the number of students in the class. Realistically a 422 class is no larger than 40 students. But in current testing, every addition to the number of students vastly increases the runtime of calculating optimal teams.
	RESULTS: PASSED on a test sample of 90 students, time < 10 seconds. On any number of students greater than 90, my personal machine (macOS) hits a maximum recursion depth error, which is a Python setting that can be changed.

too_small.csv -> The number of students in the class is smaller than the number of students needed on a team. In this case, it should create only one teamwhere the students are put on the team no matter their differences.
	RESULTS: PASSED. program sorts exactly as expected. With only two students, the algorithm creates one team with both the students on it. time < 1 second.
