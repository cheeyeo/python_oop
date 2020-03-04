import abc

class Assignment(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def lesson(self):
		pass

	@abc.abstractmethod
	def check(self, code):
		pass

	@classmethod
	def __subclasshook__(cls, C):
		if cls is Assignment:
			attrs = set(dir(C))
			if set(cls.__abstractmethods__) <= attrs:
				return True

		return NotImplemented