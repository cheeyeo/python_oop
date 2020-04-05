def setup_module(module):
	print("Setting up MODULE {0}".format(module.__name__))

def teardown_module(module):
	print("Tearing down MODULE {0}".format(module.__name__))

def test_a_function():
	print("RUNNING TEST FUNCTION")

class BaseTest:
	def setup_class(cls):
		print("Setting up CLASS {0}".format(cls.__name__))

	def teardown_class(cls):
		print("Tearing down CLASS {0}".format(cls.__name__))

	def setup_method(self, method):
		print("Setting up METHOD {0}".format(method.__name__))

	def teardown_method(self, method):
		print("Tearing down METHOD {0}".format(method.__name__))

class TestClass1(BaseTest):
	def test_method_1(self):
		print("RUNNING METHOD 1-1")

	def test_method_2(self):
		print("RUNNING METHOD 1-2")

class TestClass2(BaseTest):
	def test_method_1(self):
		print("RUNNING METHOD 2-1")

	def test_method_2(self):
		print("RUNNING METHOD 2-2")