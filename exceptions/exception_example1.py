def no_return():
	print("I'm about to raise an exception")
	raise Exception("An error occured!")

def funny_division(divider):
	try:
		return 100 / divider
	except ZeroDivisionError:
	  return "Zero is not a good idea"


print(funny_division(0))
print(funny_division("hello"))

# try:
# 	no_return()
# except:
# 	print("I caught an exception")

# print("Executed after exception caught")

