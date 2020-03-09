# Example on the use of property keyword

class Color:
	def __init__(self, rgb_value, name):
		self.rgb_value = rgb_value
		self._name = name

	def _set_name(self, name):
		if not name:
			raise Exception("Invalid Name")
		self._name = name

	def _get_name(self):
		return self._name

	name = property(_get_name, _set_name)

if __name__ == "__main__":
	c = Color("#0000ff", "red")
	print(c.name)

	c.name = ""