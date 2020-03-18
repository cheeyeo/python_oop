# Custom class which implements __lt__ for sorting

class WeirdSortee:
	def __init__(self, string, num, sort_num):
		self.string = string
		self.num = num
		self.sort_num = sort_num

	def __lt__(self, other):
		if self.sort_num:
			return self.num < other.num
		return self.string < other.string

	def __repr__(self):
		return f"{self.string}:{self.num}"
