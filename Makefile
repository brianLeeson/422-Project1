SOURCES = groupApp.py

run:  $(SOURCES)
	python3 groupApp.py &

pullmaster:
	git pull origin master

pullamie:
	git pull origin amie

pullbrian:
	git pull origin brian

pulljamie:
	git pull origin jamie

locUp:
	git checkout ${BRANCH}
	git pull origin ${BRANCH}
	git pull origin master

	git push origin ${BRANCH}

mastUp: locUp
	git checkout master
	git pull origin master
	git pull origin ${BRANCH}
	git commit -am "make file commit"
	git push origin master
	git checkout ${BRANCH}
	git pull origin master
	

