# Statistics class extend the Assignment abstract class directly
from assignment import Assignment

class Statistics(Assignment):
	def lesson(self):
		return (
			"Good work so far, "
			+ self.student 
			+ ". Now calculate the average of the numbers "
			+ "1, 5, 18, -3 and assign to a variable named 'avg'"
		)

	def check(self, code):
		import statistics

		code = "import statistics\n" + code

		local_vars = {}
		global_vars = {}
		exec(code, global_vars, local_vars)

		return local_vars.get("avg") == statistics.mean([1, 5, 18, -3])
