from random import randint 
from sys import exit
def lotto(rangemax):
	lottomoney = rangemax * 3.2
	print "You can win up to $%.2f !!" % lottomoney
	a = int(raw_input("1. "))
	b = int(raw_input("2. "))
	c = int(raw_input("3. "))
# change lotto ranges
	ra = rangemax
	rb = rangemax - 1
	rc = rangemax - 2
	diffa = abs(ra - a)
	diffb = abs(rb - b)
	diffc = abs(rc - c)
	print rangemax
	print "The numbers are %d, %d and %d" % (ra, rb, rc)
	print "You were off by %d, %d and %d respectively" % (diffa, diffb, diffc)
	if a== ra and b == rb and c == rc:
		print "####### YOU WON %.2f #########" % lottomoney
	elif a == ra and b == rb:
		print "####### YOU WON %.2f #########" % (lottomoney / 2)
	elif a == ra and c == rc:
		print "####### YOU WON %.2f #########" % (lottomoney / 2)
	elif b == rb and c == rc:
		print "####### YOU WON %.2f #########" % (lottomoney / 2)
	elif a == ra or b == rb or c == rc:
		print "####### YOU WON %.2f #########" % (lottomoney / 4)
	else:
		print "Sorry none of those numbers are winners :("
		#tryagain = raw_input("Would you like to try again?: ")
		#if tryagain == "yes":
		#	lotto(
		#		raw_input("1. "),
		#		raw_input("2. "),
		#		raw_input("3. "))
		#else:
		#	exit(0)
lotto(
	int(raw_input(
		"Choose a maximum range for the lottery numbers and enter three numbers. ")))