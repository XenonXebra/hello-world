def calculate_tax(original_price, tax):
	if len(original_price) >= 1 and len(tax) >= 1:
		print "-" * 15
		print "Tax rate: " + tax + "%"
		tax_multiplier1 = float(tax) * 0.01
		tax_multiplier2 = tax_multiplier1 * float(original_price)
		total = float(original_price) + float(tax_multiplier2)
		totalr = round(float(total), 2)
		print "Total Price after tax: $%.2f" % totalr

calculate_tax(
	raw_input("Enter the original price: "), 
	raw_input("Enter the tax rate as a percentage (ignore the sign): "))