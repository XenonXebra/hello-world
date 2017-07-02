def calculate_change(cost, paid):
	change = float(paid) - float(cost)
	print "-" * 10
	print "You should receive $%.2f" % change
	print "-" * 10
	ten_notes = change * 0.1
	print "$10 notes: " + str(int(ten_notes))
	if int(ten_notes) >= 1:
		ten_five_diff = change - int(ten_notes) * 10
		five_coins = ten_five_diff * 0.2
		print "$5 coins: " + str(int(five_coins))
		five_two_diff = ten_five_diff - int(five_coins) * 5
		two_coins = five_two_diff * 0.5
		print "$2 coins: %d" % two_coins
		two_one_diff = five_two_diff - int(two_coins) * 2
		#one_coins = two_one_diff
		print "$1 coins: %d" % two_one_diff
	else:
		five_coins = change * 0.2
		print "$5 coins: " + str(int(five_coins))
		five_two_diff = change - int(five_coins) * 5
		two_coins = five_two_diff * 0.5
		print "$2 coins: %d" % two_coins
		two_one_diff = five_two_diff - int(two_coins) * 2
		print "$1 coins: %d" % two_one_diff

calculate_change(
	raw_input("Cost of product: "), 
	raw_input("Amount paid: "))