import datetime
import time

class TimedEvent:
	def __init__(self, end_time, callback):
		self.end_time = end_time
		self.callback = callback

	def ready(self):
		return self.end_time <= datetime.datetime.now()

class Timer:
	def __init__(self):
		self.events = []

	def call_after(self, delay, callback):
		end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)

		self.events.append(TimedEvent(end_time, callback))

	def run(self):
		while True:
			ready_events = [e for e in self.events if e.ready()]
			for event in ready_events:
				event.callback(self)
				self.events.remove(event)
			time.sleep(0.5)

def format_time(message, *args):
	now = datetime.datetime.now()
	print(f"{now:%I:%M:%S}: {message}")

class Repeater:
	def __init__(self):
		self.count = 0

	# Makes Reapter a callable object by implementing __call__
	# takes the timer object passed in callback
	# and invokes it again
	def __call__(self, timer):
		format_time(f"repeat {self.count}")
		self.count += 1
		timer.call_after(5, self)



if __name__ == "__main__":
	def one(timer):
		print("ONe function called!")


	timer = Timer()
	timer.call_after(1, one)
	timer.call_after(2, one)
	timer.call_after(5, Repeater())
	timer.run()