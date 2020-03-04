def funny_division3(divider):
	try:
		if divider == 13:
			raise ValueError("13 is an unlucky number")
		return 100 / divider
	except ZeroDivisionError:
		return "Enter a number other than 0"
	except TypeError:
		"Enter a numerical value"
	except ValueError:
		print("Not 13")
		raise # passes it back to calling function where exception originated...

funny_division3(13)