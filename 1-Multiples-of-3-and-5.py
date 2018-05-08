### PROJECT EULER

#Problem 1

numbersToAdd = []

def addTo(number):
	count = 0
	while count < number:
		if count % 3 == 0 or count % 5 == 0:
			numbersToAdd.append(count)
		count = count + 1
	#print(numbersToAdd)
	print(sum(numbersToAdd))
addTo(1000)