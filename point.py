import math

class Point:
	"Represents a point in 2d geometric coordinates"

	def __init__(self, x=0, y=0):
		"""
		Initialize the position of a new point. The x and y coordinates can be specified. 

		If not, it defaults to the origin."""
		self.move(x, y)

	def move(self, x, y):
		"""Move the point to new location in 2d space"""
		self.x = x
		self.y = y

	def reset(self):
		"""Reset point back to origin, 0:0"""
		self.x = 0
		self.y = 0

	def calculate_distance(self, other_point):
		"""Calculate distance from this point to a second point passed as a parameter.

		Uses the pythagorean theorem to calculate distance between the two points.

		The distance is returned as a float.
		"""

		return math.sqrt(
			(self.x - other_point.x) ** 2
			+ (self.y - other_point.y) ** 2
		)