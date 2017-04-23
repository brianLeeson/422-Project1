#!/usr/bin/env bash
SHELL := /bin/bash
# Author(s): Brian

SOURCES = groupApp.py
VENV = python3 -m venv

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
	

