#Problem 2

sequence = []
evens = []
limit = 4000000

#code could be cleaner
#make it one function or 2?

def fibonacci(terms):
	for i in range(terms):
		if i == 0 or i == 1:
			sequence.append(i)
		else:
			sequence.append(sequence[i-1]+sequence[i-2])
			if sequence[i] > limit:
				break
	print(sequence)

def evenFibonacci(sequence):
	for i in sequence:
		if i % 2 == 0:
			evens.append(i)
	print(evens)
	print(sum(evens))

fibonacci(40)
evenFibonacci(sequence)