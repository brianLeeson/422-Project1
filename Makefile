# Author Brian

SOURCES = groupApp.py

run:  $(SOURCES)
	python3 groupApp.py &

#
# locUp and mastUp will NOT commit for you. make sure you commit your branch changes.
# if either fails, check your commits

locUp:
	git checkout ${BRANCH}
	git pull origin ${BRANCH}
	git pull origin master
	git push origin ${BRANCH}

mastUp: locUp
	git checkout master
	git pull origin master
	git pull origin ${BRANCH}
	git push origin master
	git checkout ${BRANCH}
	git pull origin master
	

