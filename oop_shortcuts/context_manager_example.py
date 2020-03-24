# Example of a context manager which takes a list of strings and returns a single joined string on exit

class StringJoiner(list):
	# called after 'as' in 'with' block
	def __enter__(self):
		return self

	# called after 'with' block exits
	def __exit__(self, type, value, tb):
		# type, value, tb has values only when exception thrown
		self.result = "".join(self)

if __name__ == "__main__":
	import random
	import string

	with StringJoiner() as joiner:
		for i in range(15):
			joiner.append(random.choice(string.ascii_letters))

	print(joiner.result)