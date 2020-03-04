import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
	choice = random.choice(some_exceptions)
	print("Raising {}".format(choice))
	if choice:
		raise choice("An error")
except ValueError:
	print("Caught ValueError")
except TypeError:
	print("Caught TypeError")
except Exception as e:
	print("Caught some other error: {}".format(e.__class__.__name__))
else:
	print("This code called if there's no exception")
finally:
	print("This is always called")