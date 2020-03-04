# Example of multiple inheritance which uses super() to call parent method only once

class BaseClass:
	num_base_calls = 0

	def call_me(self):
		print("Calling method on Base Class.")
		self.num_base_calls += 1

class LeftSubclass(BaseClass):
	num_left_calls = 0

	def call_me(self):
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls += 1

class RightSubclass(BaseClass):
	num_right_calls = 0

	def call_me(self):
		super().call_me()
		print("Calling method on Right subclass")
		self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0

	def call_me(self):
		super().call_me()
		print("Calling method on subclass")
		self.num_sub_calls += 1

s = Subclass()
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)

"""
Calling method on Base Class.
Calling method on Right subclass
Calling method on Left Subclass
Calling method on subclass
1 1 1 1
"""