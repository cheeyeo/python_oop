# Example of using Container abstract class from Collections module

from collections import Container
# print(Container.__abstractmethods__)
# print(help(Container.__contains__))

class OddContainer:
	def __contains__(self, x):
		if not isinstance(x, int) or not x % 2:
			return False

		return True

if __name__ == "__main__":
	odd_container = OddContainer()
	print(isinstance(odd_container, Container))
	print(issubclass(OddContainer, Container))
	print(1 in odd_container)
	print(2 in odd_container)