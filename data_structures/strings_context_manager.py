# Example of creating a custom context manager object to be used in a with loop
# Implements the __enter__ and __exit__ methods

class StringJoiner(list):
	def __enter__(self):
		return self

	def __exit__(self, type, value, tb):
		self.result = "".join(self)


if __name__ == "__main__":
	import random
	import string

	with StringJoiner() as joiner:
		for i in range(15):
			joiner.append(random.choice(string.ascii_letters))

	# once outside of context, __exit__ will be called and the result attribute is set
	print(joiner.result)