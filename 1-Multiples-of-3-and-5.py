### PROJECT EULER

#Problem 1

numbersToAdd = []

def addTo(number):
	for i in range(number):
		if i % 3 == 0 or i % 5 == 0:
			numbersToAdd.append(i)
	print(sum(numbersToAdd))

addTo(1000)