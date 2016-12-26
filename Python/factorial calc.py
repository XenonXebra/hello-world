def find_factorial(n):
		m = abs(int(n))
		total = 1
		while m > 0:
			total = int(total) * int(m)
			m -= 1
		print str(n) + "! is "  + str(total)


find_factorial(raw_input("Enter a number to find its factorial: "))