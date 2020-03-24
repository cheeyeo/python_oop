def my_function():
	print("MY FUNCTION WAS CALLED!")

my_function.description = "My Function"

def another_function():
	print("ANOTHER FUNCTION WAS CALLED")

another_function.description = "Another Function"

def some_other_function(func):
	print("Description=", end=" ")
	print(func.description)
	print("Name= ", end=" ")
	print(func.__name__)
	print("Class= ", end=" ")
	print(func.__class__)
	print("Calling actual func: ", end=" ")
	func()

some_other_function(my_function)
some_other_function(another_function)