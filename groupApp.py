"""
Author(s): Brian Leeson

"""

import Classroom
import tkinter as tk
from tkinter import filedialog
import fileProcess as fp

# WISHLIST - in order
# APPA
# weight labels and sliders

# Classroom instance stores data
CLASSROOM = Classroom.Classroom("0", "")  # Global variable instance
PATH = ""  # path to import csv


# DEFINE FUNCTIONS
def importCB():
		"""
		called when import button clicked
		function prompts user to select path to csv 
		and processes csv
		"""
		global PATH

		# prompt user for path
		PATH = filedialog.askopenfilename()

		# files process
		if len(PATH):  # if they picked something
			print("imported")

		return None


def sortCB():
		"""
		Function calls sort on classroom class.
		"""
		global CLASSROOM
		global PATH

		# Get Field Values
		size = int(numStudentSpin.get())
		name = nameEntry.get()
		crn = crnEntry.get()
		# TODO: set teamsize when size of !3 is allowed
		# classroom.setTeamSize(size)

		# create new Classroom instance. overwrites global
		CLASSROOM = Classroom.Classroom(crn, name)

		# files process
		if len(PATH):  # if they picked something
			studentCollection = fp.process(PATH)

			# assign to classroom class
			CLASSROOM.setStudentList(studentCollection)

		CLASSROOM.sortIntoTeams()
		print("sorted")

		display()

		return None


def display():
	"""
	this function displays the currently sorted teams on the canvas
	"""
	global CLASSROOM

	# --- Make and display team string
	tCount = 0
	row = 0
	col = 0
	for team in CLASSROOM.teamList:
		teamText = "TeamID: " + str(team.getNumber()) + "\n"
		for student in team.getMemberList():
			teamText += student.getName() + "\n"
		teamText += "Quality score: " + str(team.quality_score)

		teamLabel = tk.Label(canvasFrame, text=teamText, bd=4, highlightthickness=7, justify=tk.LEFT, relief=tk.GROOVE)
		teamLabel.grid(row=row, column=col)

		row = (tCount + 1) // 4
		col = (col + 1) % 4
		tCount += 1

	return None


def exportCB():
		"""
		Function exports csv of sorted teams to csv
		"""
		fp.export(CLASSROOM.getTeamList())

		print("exported")

		return None


# create app
app = tk.Tk()

mainFrame = tk.Frame(app, bd=1, relief=tk.SUNKEN)
mainFrame.grid(row=0, column=0)

# --- Frame 0 --- Name
nameFrame = tk.Frame(mainFrame, bd=1)
nameFrame.grid(row=0, column=0, columnspan=3)

nameLabel = tk.Label(nameFrame, text="Instructor: ")
nameLabel.grid(row=0, column=0)

nameEntry = tk.Entry(nameFrame)
nameEntry.grid(row=0, column=1)

# --- Frame 1 --- CRN
crnFrame = tk.Frame(mainFrame, bd=1)
crnFrame.grid(row=1, column=0, columnspan=3)

crnLabel = tk.Label(crnFrame, text="CRN: ")
crnLabel.grid(row=0, column=0)

crnEntry = tk.Entry(crnFrame)
crnEntry.grid(row=0, column=1)

# --- Frame 2 --- numstudent
numStudentFrame = tk.Frame(mainFrame, bd=1)
numStudentFrame.grid(row=2, column=0, columnspan=3)

numStudentLabel = tk.Label(numStudentFrame, text="Group Size: ")
numStudentLabel.grid(row=0, column=0)

numStudentSpin = tk.Spinbox(numStudentFrame, from_=2, to=6)
numStudentSpin.delete(0, 2)
numStudentSpin.insert(0, 3)
numStudentSpin.grid(row=0, column=1)

# --- Frame 3 --- DESCRIPTION
description = tk.Frame(mainFrame, bd=1)
description.grid(row=3, column=0, columnspan=3)

descriptionText = "Surveys in csv form can be imported, sorted into teams and" \
					" exported as a csv for further changes if needed."
descriptionLabel = tk.Label(description, text=descriptionText, wraplength=200)
descriptionLabel.grid(row=0, column=0)

# --- Frame 4 --- BUTTONS
processFrame = tk.Frame(mainFrame, bd=1, relief=tk.SUNKEN)
processFrame.grid(row=4, column=0, columnspan=3)

importButton = tk.Button(processFrame, text="import", command=importCB)
importButton.grid(row=0, column=0)

sortButton = tk.Button(processFrame, text="sort", command=sortCB)
sortButton.grid(row=0, column=1)

exportButton = tk.Button(processFrame, text="export", command=exportCB)
exportButton.grid(row=0, column=2)

# --- Canvas
canvasFrame = tk.Frame(mainFrame, bd=1, width=500, height=230, bg="white")
canvasFrame.grid(row=0, column=3, rowspan=5)

# runs the app
app.mainloop()
