"""
Author(s): Jamie Zimmerman

"""

import csv
import datetime
import string
import random


def generate_students(people, csv_name):
	
	with open(csv_name, 'w') as csvfile:
		fieldnames = ['Timestamp', 'Student Name', 'Your DuckID', 'Python experience', 'Java experience', 'Javascript experience', 'C experience', 'C++ experience', 'PHP experience', 'HTML experience', 'SQL experience', 'Bash/Unix experience', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Desired Teammates DuckIDs (separated by ';')"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		
		possible_times = ["10:00 - 12:00;2:00 - 4:00;", "10:00 - 12:00;12:00 - 2:00", "2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00",
						"12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00;4:00 - 6:00",
						"10:00 - 12:00", "None", "12:00 - 2:00", "2:00 - 4:00", "4:00 - 6:00", "2:00 - 4:00;4:00 - 6:00"]
		for i in range(people):
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

def generate_no_pairings():
	with open("no_pairings_extreme.csv", 'w') as csvfile:
		fieldnames = ['Timestamp', 'Student Name', 'Your DuckID', 'Python experience', 'Java experience', 'Javascript experience', 'C experience', 'C++ experience', 'PHP experience', 'HTML experience', 'SQL experience', 'Bash/Unix experience', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Desired Teammates DuckIDs (separated by ';')"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		
		possible_times = ["10:00 - 12:00;2:00 - 4:00;", "10:00 - 12:00;12:00 - 2:00", "2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00", 
						"12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "12:00 - 2:00;2:00 - 4:00",
						"12:00 - 2:00;2:00 - 4:00", "12:00 - 2:00;2:00 - 4:00;4:00 - 6:00", "None", "10:00 - 12:00;12:00 - 2:00;2:00 - 4:00", "2:00 - 4:00;4:00 - 6:00",
						"10:00 - 12:00", "None", "12:00 - 2:00", "2:00 - 4:00", "4:00 - 6:00", "2:00 - 4:00;4:00 - 6:00"]
		for i in range(30):
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
			
			mon = "None"
			tues = "None"
			wed ="None"
			thurs ="None"
			fri ="None"

			teammate = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + "; " + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
			writer.writerow({'Timestamp': time, 'Student Name': name, 'Your DuckID': duckid, 'Python experience': python, 'Java experience': jav, 'Javascript experience': js,
							'C experience': c, 'C++ experience': cpp, 'PHP experience': php, 'HTML experience': html, 'SQL experience': sql, 'Bash/Unix experience': bash,
							'Monday': mon, 'Tuesday': tues, 'Wednesday': wed, 'Thursday': thurs, 'Friday': fri, "Desired Teammates DuckIDs (separated by ';')": teammate})
	return None

# ------------------------------------------------------------
if __name__ == '__main__':
	generate_students(90, 'too_big.csv')
	#generate_students(2, 'too_small.csv')
	#generate_students(10, 'one_extra.csv')
	#generate_students(20, 'two_extra.csv')
	#generate_students(4, 'odd_one_out.csv')
	#generate_no_pairings()






