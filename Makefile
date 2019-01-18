tenThousand: race.cc runRace.py
	g++ race.cc -pthread
	python runRace.py

one: race.cc
	g++ race.cc -pthread
	./a.out
