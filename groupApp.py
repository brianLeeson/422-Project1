"""
Author(s): Brian Leeson

"""

import Classroom
import tkinter as tk
from tkinter import filedialog
import fileProcess as fp


# TODO: Should we consider a manual entry? what if google forms doesn't work?

# create window
# window has:
# import csv button - should auto processes.
# sort button
# export to csv button

# WISHLIST - in order
# APPA
# students per group slider
# weight labels and sliders
# "screen" to view results

# Classroom instance stores data
classroom = Classroom.Classroom(12345, "Your boi")  # Global variable instance, might need to overwrite in importCB


# DEFINE FUNCTIONS
def importCB():
		"""
		called when import button clicked
		function prompts user to select path to csv and
		process csv
		"""

		# create new Classroom instance. overwrites global on purpose
		# classroom = Classroom.Classroom(12345, "Teacher Name")

		# prompt user for path
		path = filedialog.askopenfilename()

		# files process
		if len(path):  # if they picked something
			studentCollection = fp.process(path)

			# assign to classroom class
			classroom.setStudentList(studentCollection)

			print("imported")

		return None


def sortCB():
		"""
		Function calls sort on classroom class.
		"""

		# TODO: set group size here

		classroom.sortIntoTeams()

		print("sorted")

		return None


def exportCB():
		"""
		Function exports csv of sort teams to cwd
		"""
		# TODO: Need function in file process to call
		fp.export(classroom.getTeamList())

		print("exported")

		return None


# create app
app = tk.Tk()

mainFrame = tk.Frame(app, bd=1, relief=tk.SUNKEN)
mainFrame.grid(row=0, column=0)

# --- Frame 0
nameFrame = tk.Frame(mainFrame, bd=1)  # TODO: types of relief?
nameFrame.grid(row=0, column=0, columnspan=3)

nameLabel = tk.Label(nameFrame, text="Name:")
nameLabel.grid(row=0, column=0)

nameEntry = tk.Entry(nameFrame)
nameEntry.grid(row=0, column=1)

# --- Frame 1
crnFrame = tk.Frame(mainFrame, bd=1)
crnFrame.grid(row=1, column=0, columnspan=3)

crnLabel = tk.Label(crnFrame, text="CRN:")
crnLabel.grid(row=0, column=0)

crnEntry = tk.Entry(crnFrame)
crnEntry.grid(row=0, column=1)

# --- Frame 2
numStudentFrame = tk.Frame(mainFrame, bd=1)
numStudentFrame.grid(row=2, column=0, columnspan=3)

numStudentLabel = tk.Label(numStudentFrame, text="Group Size:")
numStudentLabel.grid(row=0, column=0)

numStudentSpin = tk.Spinbox(numStudentFrame, from_=1, to=5)
numStudentSpin.grid(row=0, column=1)

# --- Frame 3
description = tk.Frame(mainFrame, bd=1)
description.grid(row=3, column=0, columnspan=3)

descriptionLabel = tk.Label(description, text="DESCRIPTION HERE")
descriptionLabel.grid(row=0, column=0)

# --- Frame 4
processFrame = tk.Frame(mainFrame, bd=1, relief=tk.SUNKEN)
processFrame.grid(row=4, column=0, columnspan=3)

importButton = tk.Button(processFrame, text="import", command=importCB)
importButton.grid(row=0, column=0)

sortButton = tk.Button(processFrame, text="sort", command=sortCB)
sortButton.grid(row=0, column=1)

exportButton = tk.Button(processFrame, text="export", command=exportCB)
exportButton.grid(row=0, column=2)


# --- Canvas
canvasFrame = tk.Frame(mainFrame, bd=1)
canvasFrame.grid(row=0, column=3, rowspan=5)

canvas = tk.Canvas(canvasFrame, width=500, height=500, borderwidth=10, bg="white")
canvas.grid(row=0, column=1)


# runs the app
app.mainloop()
