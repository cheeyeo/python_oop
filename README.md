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

* Empty object => can instantiate an object without defining a class
```
o = object()

# cannot set attrs on it!
o.x = 5
```

From above, we can't set arbitray attributes on object instantiated directly; python allocates memory to track the attribute names and values for each object; hence it disables arbitrary properties on objects and other built-in types

* Possible to restrict arbitrary properties on classes using slots

* can create empty object of custom class:
```
class MyClass:
  pass


m = MyClass()
m.x = "hello"
m.x # => "hello"
```

* Tuples immutable; can't modify objects in tuple

* Tuples are used to store data; behaviour cannot be associated with tuple

	If we require behaviour to manipulate a tuple, pass the tuple into a function

* Tuples store values which are different from each other e.g.
```
stock = ("STOCK 1", 177.2, 177.3)
```

* Can access tuple values directly or by using a slice:
```
tuple[2]

tuple[1:3]
```

* Named Tuples group read-only data

* To create named tuples, we use collections.namedtuple to create a class and create instances of that class

* Like ordinary tuples, its immutable so we can't add attributes or modify its value

* Dataclasses => regular objects for defining attributes

* Dictionaries allow mapping of objects to other objects

* Objects represent attributes as dictionaries where the values are properties or methods on the object ( obj.__dict__ )

* Technically, most Python objects are implemented using dictionaries under the hood. You can see this by loading an object into the interactive interpreter and looking at the obj.__dict__ magic attribute. 

When you access an attribute on an object using obj.attr_name, it essentially translates the lookup to obj['attr_name'] under the hood

* We should typically use dataclasses when we know exactly what attributes the data must store, especially if we also want to use the class definition as documentation for the end user.