# Custom class which implements __lt__ and __eq__ for sorting and using custom operators for comparison

from functools import total_ordering

@total_ordering
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

	def __eq__(self, object):
		return all((
			self.string == object.string,
			self.num == object.num,
			self.sort_num == object.sort_num
		))