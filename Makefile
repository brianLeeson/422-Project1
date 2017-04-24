#!/usr/bin/env bash
SHELL := /bin/bash
# Author(s): Brian

SOURCES = groupApp.py
VENV = python3 -m venv

# User instructions:
# In order to construct and run this project type "make run" into the shell window
# This should create the virtual environment and install any dependencies,
# finally running the application. To quit the application, simply close out of the window.

# To add a dependency to this project:
# create the virtual environment with "make env"
# go into the virtual environment with "source ./env/bin/activate"
# install any new dependencies
# use "make freeze" to write the state to requirements.txt
# get out of the virtual environment with "deactivate"

env:
	$(VENV) ./env
	(source ./env/bin/activate; pip install -r requirements.txt) || true

freeze:
	(pip freeze | grep -v "pkg-resources" > requirements.txt) || true

run: env
	. env/bin/activate; python3 groupApp.py > log.txt

clean:
	rm -rf __pycache__
	rm -f team_decisions.csv

veryclean:
	make clean
	rm -rf env
	clear > log.txt

# Developer tools
#
# when using mastUp and locUp, make sure that the recipe did not fail by reading the last line.
# locUp and mastUp will NOT commit for you. make sure you commit your branch changes.
# if either command fails, check your commits
#
# usage: make BRANCH="branch_name" locUp/mastUp

# updates local directory with most recent code
locUp:
	git checkout ${BRANCH}
	git pull origin ${BRANCH}
	git pull origin master
	git push origin ${BRANCH}

# updates master by merging branch_name with master
mastUp: locUp
	git checkout master
	git pull origin master
	git pull origin ${BRANCH}
	git push origin master
	git checkout ${BRANCH}
	git pull origin master
	

