SOURCES = groupApp.py

run:  $(SOURCES)
	python3 groupApp.py &

locUp:
	git checkout ${BRANCH}
	git pull origin ${BRANCH}
	git pull origin master
	git commit -am "make file commit"
	git push origin ${BRANCH}

mastUp: locUp
	git checkout master
	git pull origin master
	git pull origin ${BRANCH}

	git push origin master
	git checkout ${BRANCH}
	git pull origin master
	

