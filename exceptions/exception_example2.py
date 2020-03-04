def funny_division2(divider):
	try:
		if divider == 13:
			raise ValueError("13 is an unlucky number")
		return 100 / divider
	except (ZeroDivisionError, TypeError):
		return "Enter a number other than 0!"

for val in (0, "hello", 50.0, 13):
	print("Testing: {}".format(val), end=" ")
	print(funny_division2(val))
