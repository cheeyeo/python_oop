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