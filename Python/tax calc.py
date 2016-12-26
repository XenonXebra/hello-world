def calculate_tax(original_price, tax):
	if len(original_price) >= 1 and len(tax) >= 1:
		print "-" * 15
		print "Tax rate: " + tax + "%"
		tax_multiplier1 = int(tax) * 0.01
		tax_multiplier2 = tax_multiplier1 * int(original_price)
		total = int(original_price) + int(tax_multiplier2)
		print "Total Price after tax: $%d" % total

calculate_tax(
	raw_input("Enter the original price: "), 
	raw_input("Enter the tax rate as a percentage (ignore the sign): "))