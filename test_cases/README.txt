#test_cases/

This folder contains various sample inputs meant to test the robustness of the sorting algorithm.

generate.py -> this script writes the csv files. It creates random strings for names, random numbers for coding skills, and chooses randomly from a list of time availability combinations. This script should not be used any more, as it has already created the below sample class inputs.

no_pairings_extreme.csv -> a classroom where every student has literally NO time availability, has listed "None" for every one of their meeting times. This situation is wildly unrealistic to happen in real-life.

no_pairings.csv -> a classroom where very few people have any meeting times, i.e. most people can only meet once per week.

odd_one_out.csv -> When team sizes are only 3, and there are 4 students in the class. This should create one team of 4.

one_extra.csv -> The number of students in the class is a multiple of 3 + 1 more student. So this should create only one team of 4.

two_extra.csv -> The number of students in the class is a multiple of 3 + 2 more students. So this should create two teams of 4.

too_big.csv -> Tests the upper limit on the number of students in the class. Realistically a 422 class is no larger than 40 students. But in current testing, every addition to the number of students vastly increases the runtime of calculating optimal teams.
	RESULTS: At a test sample of 100 students, this program runs too slowly to be usable. Upon sorting into teams, the algorithm runs indefinitely and never comes to a decision (waited approximately 5 minutes before killing the program manually).

too_small.csv -> The number of students in the class is smaller than the number of students needed on a team. In this case, it should create only one teamwhere the students are put on the team no matter their differences.
	RESULTS: program sorts exactly as expected. With only two students, the algorithm creates one team with both the students on it.
