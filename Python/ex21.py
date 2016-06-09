def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "MULTIPYING %d x %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 

print "Let's do some math with just functions"

print "Give two numbers that add up to give your age:"
age = add(int(raw_input("1. ")), int(raw_input("2. ")))

print "Two numbers to subtract that give your height in cm:"
height = subtract(int(raw_input("1. ")), int(raw_input("2. ")))

print "Two numbers to multiply:"
weight = multiply(int(raw_input("1. ")), int(raw_input("2. ")))

print "Two numbers to divide:"
iq = divide(int(raw_input("1. ")), int(raw_input("2. ")))


raw_input("Press ENTER to compute")

print "Age: %d, Height: %d, Weight: %d IQ: %d" % (
	age, height, weight, iq)

height2 = height ** 2
BMI = weight / height2

print "Press ENTER to compute BMI"
print "DIVIDING your weight, %d, by your height squared, %d,  ..." % (weight, height2)
print "Your BMI is: ", BMI

# A puzzle for the extra credit, type it in anyway
print "\nHere is a random puzzle."
raw_input("Press enter to continue")

print "\n"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"
