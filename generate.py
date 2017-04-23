"""
Author(s): Jamie Zimmerman

"""

from Student import Student  # from module import class
import csv
import datetime
import string
import random

#helper function to process student availability into binary representation
def create_time_chart(day_availability_list):
	"""
	input  - list of day's time slots, ex: ["10:00-12:00;2:00-4:00", "2:00-4:00;4:00-6:00", "10:00-12:00;4:00-6:00", "None", "10:00-12:00;2:00-4:00"]
		the first item in the list is Monday, then Tuesday, etc... (the function zips this with in-order days so that the data is not scrambled)
		within each 'day' is a semicolon separated list of available times slots
	this function parses that availability into a binary representation
	output - dictionary - entire dictionary representing student's availability
		key: days (Monday, Tuesday, etc.)
		value: a list of 0's and 1's, which indicates which times slots are open for that student
		ex: "Monday":[0, 1, 1, 0, 0] means that the student is available on Monday from 12:00-2:00& 2:00-4:00
		the list should only be 5 spaces long, representing 4 time slots(10-12, 12-2, 2-4, 4-6) and None, meaning no time available
		example usage: student.setAvailability(create_time_chart(day_availability_list))
	"""
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	pre_chart = dict(zip(days, day_availability_list))
	chart = dict()
	for day, daytimes in pre_chart.items():
		times = daytimes.split(';')
		new_li = [0 for i in range(5)]
		for slot in times:
			if slot == "10:00 - 12:00":
				new_li[0]=1
			elif slot == "12:00 - 2:00":
				new_li[1]=1
			elif slot == "2:00 - 4:00":
				new_li[2]=1
			elif slot == "4:00 - 6:00":
				new_li[3]=1
			else:  # No available time
				new_li[0:] = [0 for i in range(5)]
		chart[day] = new_li
	return chart


def generate_many():
	
	with open('too_big.csv', 'w') as csvfile:
		fieldnames = ['Timestamp', 'Student Name', 'Your DuckID', 'Python experience', 'Java experience', 'Javascript experience', 'C experience', 'C++ experience', 'PHP experience', 'HTML experience', 'SQL experience', 'Bash/Unix experience', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Desired Teammates DuckIDs (separated by ';')"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		
		possible_times = ["10:00 - 12:00;2:00 - 4:00;", "10:00 - 12:00;12:00 - 2:00", "2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00",
						"12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00;4:00 - 6:00",
						"10:00 - 12:00", "None", "12:00 - 2:00", "2:00 - 4:00", "4:00 - 6:00", "2:00 - 4:00;4:00 - 6:00"]
		for i in range(1000):
			time = datetime.datetime.now()
			name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
			duckid = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
			python = random.randint(0, 5)
			jav = random.randint(0, 5)
			js =random.randint(0, 5)
			c = random.randint(0, 5)
			cpp = random.randint(0, 5)
			php = random.randint(0, 5)
			html = random.randint(0, 5)
			sql = random.randint(0, 5)
			bash = random.randint(0, 5)
			
			mon = possible_times[random.randint(0,24)]
			tues = possible_times[random.randint(0,24)]
			wed =possible_times[random.randint(0,24)]
			thurs =possible_times[random.randint(0,24)]
			fri =possible_times[random.randint(0,24)]

			teammate = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + "; " + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
			writer.writerow({'Timestamp': time, 'Student Name': name, 'Your DuckID': duckid, 'Python experience': python, 'Java experience': jav, 'Javascript experience': js,
							'C experience': c, 'C++ experience': cpp, 'PHP experience': php, 'HTML experience': html, 'SQL experience': sql, 'Bash/Unix experience': bash,
							'Monday': mon, 'Tuesday': tues, 'Wednesday': wed, 'Thursday': thurs, 'Friday': fri, "Desired Teammates DuckIDs (separated by ';')": teammate})
	return None

# ----------------------Sandbox Area--------------------------------------
if __name__ == '__main__':
	# THIS CODE NEVER NEEDS TO BE SAVED, JUST A WORKSPACE AREA
	generate_many()