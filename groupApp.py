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
classroom = Classroom.Classroom(12345, "Your boi")


# DEFINE FUNCTIONS
def importCB():
		"""
		called when import button clicked
		function prompts user to select path to csv and
		process csv
		"""
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

mainFrame = tk.Frame(app)
mainFrame.grid(row=0, column=0)

importButton = tk.Button(mainFrame, text="import", command=importCB)
importButton.grid(row=0, column=0)

sortButton = tk.Button(mainFrame, text="sort", command=sortCB)
sortButton.grid(row=1, column=0)

exportButton = tk.Button(mainFrame, text="export", command=exportCB)
exportButton.grid(row=2, column=0)

canvas = tk.Canvas(app, width=500, height=500, borderwidth=10, bg="white")
canvas.grid(row=0, column=1)

# runs the app
app.mainloop()
