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

* When to use lists:
	to store instances of same types of object

	store items in some kind of order, either when inserted or sort by some other criteria

* Define `__lt__` method on objects to allow for custom sorting in list

	`sort` method will invoke `__lt__` to determine the order; `__lt__` method should return either True/False

* To customize only the sort order, can pass `key` argument into sort:

	```
	l = ["hello", "HELP", "Helo"]

  l.sort() # => ["HELP", "Helo", "hello"]; default behaviour is to return uppercase then lowercase

  l.sort(key=str.lower) # => downcase all items in list then sort; returns ['hello', 'Helo', 'HELP']

	```

* To sort based on other items than first item in list, use `operator.itemgetter` method:

```
from operator import itemgetter

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]

l.sort(key=itemgetter(1))

l # => [('p', 1), ('y', 2), ('t', 3), ('h', 4), ('o', 5), ('n', 6)]
```

Above uses itemgetter to sort by second element in tuple the numbers

* Sets are used to enforce uniqueness within a data set; sets can only contain 1 copy of each data item

* Items added to a set are not ordered; need to convert them into a list first and apply `sort` method

* Sets can operate on other sets using methods such as `union`, `intersection`, `symmetric_difference`

* When using set to check for membership, it only takes O(1) time as it hashes the value and checks for membership i.e. set will find the value in same amount of time no matter how big dataset becomes; for lists we have to iterate over each item and compare them, which can take up to O(N) time


================================================================================

* Functions are also objects which can be called and passed into other functions


* Useful builtin functions from `__builtins__` module:
	
	* len()
	* reversed()
	* enumerate()
	* all(), any()
	* eval(), exec(), compile() => runs strings as code inside interpreter
	* hasattr, setattr, getattr, deleteattr => allows object attributes to be manipulated by their string names
	* zip() => takes 2 sequences and returns a new sequence of tuples

  more functions can be found via `dir(__builtins__)`

* If we run dir on a file-like object, we see that it has two special methods named __enter__ and __exit__. 

These methods turn the file object into what is known as a `context manager`. 

Basically, if we use a special syntax called the `with` statement, these methods will be called before and after nested code is executed. On file objects, the __exit__ method ensures the file is closed, even if an exception is raised

*  Context managers are useful for the common pattern of sandwiching a piece of code between two method calls

* Method Overloading

	Implement single method that takes default/optional params to allow it to accept different argument types, rather than separate function for each type...

* Unpacking args:
	
	Use ** to pass dict to function to unpack

	If we have two dicts we want to merge and one of them is a default, we can use the ** to unpack the dict as follows:

	```
	x = {'a': 1, 'b': 2}
	y = {'b': 11, 'c': 3}
	z = {**x, **y} # z{'a': 1, 'b': 11, 'c': 3}
	```

* Can make any object callable by implementing the `__call__` method

	```
	class MyClass:
	  ...

	  def __call__(self, args):
	     ...


	# pass above as parameter to function call which will invoke the __call__ function directly

	myfunc(MyClass())
	```

	Only implement it if the object is meant to be treated like a function

	( refer to event_driven_timer2.py )

* Methods in objects/classes can also be passed as parameters or replaced by other functions on the fly

	e.g.
	```
  class A():
    def print(self):
      print("I'm class A")

  def fake_print():
    print("I'm FAKE A")

  obj = A()
  obj.print() # "I'm class A"
  obj.print = fake_print
  obj.print() # I'm FAKE A
	```

	===================================================================================

	## Strings

	* String modification methods return a brand new str object; the original input string is not modified ( strings are immutable )

	* Convert array of bytes into Unicode using `decode` method of bytes class

	* Bytes type are immutable

	* Bytesarray is mutable, can build up complex sequences of bytes from it

	```
	b = bytearray(b"abcdef")

	b[3] = ord(b"g")
	b[4] = 120

	print(b)
	```

	use `ord()` function to convert bytes to ordinal value in range 0 - 255 

## Regular Expressions

* conversion occurs for each pattern string into internal structure that makes string searching fast

if used inside a for/while loop, each conversion can slow things down...

use `re.compile` which return a compiled down object 

* Use `pickle.dump` and `pickle.load` to serialize objects to disk

	Don't pickle an entire running program or complex data object

* JSON serializer can only serialize basic types such as ints, floats, strings, lists, dictionaries

	Need to create custom json encoder classes and decoder functions for custom objects ( refer to json_example.py )

	In the json module, both the object storing and loading functions accept optional arguments to customize the behavior. The dump and dumps methods accept a poorly named cls (short for class, which is a reserved keyword) keyword argument. If passed, this should be a subclass of the JSONEncoder class, with the default method overridden. This method accepts an arbitrary object and converts it to a dictionary that json can digest. If it doesn't know how to process the object, we should call the super() method, so that it can take care of serializing basic types in the normal way.

	The load and loads methods also accept such a cls argument that can be a subclass of the inverse class, JSONDecoder. However, it is normally sufficient to pass a function into these methods using the object_hook keyword argument. This function accepts a dictionary and returns an object; if it doesn't know what to do with the input dictionary, it can return it unmodified.

## Iterator 

* Iterator an object with a `next()` method and `done()` method

* `__next__` function => accessed by `next(iterator)` built-in

* list comprehensions are faster than for loops when looping over large num of items as comprehensions are highly optimized C code

* Wrap comprehension in `()` or `{}` to create generator expression

	don't create intermediate objects when using generator expressions

	wrapping a `for` parentheses creates a generator expression

Wrapping a `for` expression in parenthesis creates a generator expression, not a tuple.

Generator expressions are frequently most useful inside function calls. For example, we can call sum, min, or max on a generator expression instead of a list, since these functions process one object at a time. We're only interested in the aggregate result, not any intermediate container.

In general, of the four options, a generator expression should be used whenever possible. 

If we don't actually need a list, set, or dictionary, but simply need to filter or convert items in a sequence, a generator expression will be most efficient. 

If we need to know the length of a list, or sort the result, remove duplicates, or create a dictionary, we'll have to use the comprehension syntax.

* Comprehensions and generator expressions can combine container construction with iteration in a single line.
```
set(c for c in arr)

{c for c in arr}

m = [(1,1), (2,2)]
{k:v for (k,v) in m}
```

* Generator objects can be constructed using the yield syntax


====================================

## Unit Testing

* use built-in unittest module

* each test method must begin with `test`

* Python's `discover` module looks for any modules in current folder or subfolders with names that start with `test` and runs them

can use CLI as follows:
```
python3-munittestdiscover
```

is above python 3.7 only?

* No need to put all tests into separate tests folder; can out test modules for different packages in a subpackage next to that package

* `pytest` runs both pytest and unittest code

* Tests written in pytest can be run using `pytest <filename>`

* print statements not shown by default for passing tests; to see output need to use `-s` flag:
`pytest <filename> -s`

* Use `coverage` to measure test coverage
```
coverage run <testfile>
```

Generates a report .coverage, which can be read using `coverage report`

* If tests are located in separate directory:
```
cd tests

pytest -vv --cov-report term-missing --cov=mymodule test_*.py
```