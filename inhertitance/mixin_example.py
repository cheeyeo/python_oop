# Example of using a mixin which is not the same as inheritance of a parent class...
# https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556

import logging

class LoggerMixin(object):
	@property
	def logger(self):
		name = '.'.join([
			self.__module__,
			self.__class__.__name__
		])
		return logging.getLogger(name)

class EssentialFunctioner(LoggerMixin, object):
	def do_the_thing(self):
		try:
			raise Exception("Yo")
		except Exception:
			self.logger.error("OH NOES")

class BusinessLogic(LoggerMixin, object):
	def __init__(self):
		super().__init__()
		# Need to set logging level else it wont print to console...
		logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
	bl = BusinessLogic()
	bl.logger.debug("Yo!")