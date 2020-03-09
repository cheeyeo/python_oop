# Python 3 OOP book

* To make a method or property as private, can prefix it with double underscore __

	performs name mangling on the attribute

	e.g

	```
	class SecretString:
	  def	__init__(self, plain_string, pass_phrase):
	    self.__plain_string = plain_string
	    self.__pass_phrase = pass_phrase

	  def decrypt(self, pass_phrase):
	    if pass_phrase == self.__pass_phrase:
	      return self.__plain_string
	    else:
	      return ""
	```

	if we try to access `secret_string.__plain_string` an error of AttributeError will be thrown

	however can still manually unmangle it:
	```
	secret_string._SecrertString__plain_string
	```

	when we use a double underscore, the property is prefixed with _<classname>

* Difference between constructor and initializer?

	constructor refers to the actual class name when creating an object??

	e.g.
	```
  p = Point() # Point() is the constructor here?
	```

	initializer refers to the `__init__` method?

* Testing if object belongs to a class:
  ```
  isinstance([], object)
  ```

* Most built-in types can be similarly extended. Commonly extended built-ins are object, list, set, dict, file, and str. 

* Using `super()` , we can ensure that classes with multiple inheritance only calls the parent class once. This is known as the `next` method

* Abstract Base Class define set of methods and properties that a class must implement to be considered a duck-type instance of that class

*  Mixins - encapsulate behaviour that can be reused in other classes

https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556

* Learn logging: https://docs.python.org/3.6/howto/logging.html

* All exceptions inherit from `BaseException`

* All exceptions must extend `BaseException` or one of its subclasses

	 ____________BaseException____________
	|									|										|
SystemExit		KeyboardInterrupt			Exception
																				|
																		Most other exceptions


* When we use `except` without specifying the exception to catch it will catch all subclasses of BaseException, including SystemExit and KeyboardInterrupt

If we want to catch all exceptions apart from those 2 special cases, use `except Exception as e:`

* Important to separate behaviour and data in OOP design

* Use `property` keyword when we want to add behaviour to data?

* Technically in Python, methods, data, properties are all attributes of a class

* Methods => callable attributes

* Properties => customizable attributes

* How to distinguish between them? Methods should represent actions; things that can be done/performed by an object

* Once confirming an attribute is not an action, we should decide between standard attributes and properties

Always use a standard attribute until we need to control access to the property in some way

Only difference between an attribute and a property is that we can invoke custom actions automatically when a property is retrieved, set or deleted

