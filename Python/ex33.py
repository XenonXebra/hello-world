numbers = []

def loop(i):
	while i < 6: # you can change this number and operation
		print "At the top i is %d" % i
		numbers.append(i)

		i += 0.5 # you can change this number
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

loop(0.05) # you can change this number 


print "The numbers: "

for num in numbers:
	print num
