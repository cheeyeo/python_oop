# Example of using a property 
# Cache webpage and storing its content on class attribute

from urllib.request import urlopen

class WebPage:
	def __init__(self, url):
		self.url = url
		self._content = None

	@property
	def content(self):
		if not self._content:
			print("Retrieving web page")
			self._content = urlopen(self.url).read()
		return self._content

if __name__ == "__main__":
	import time

	webpage = WebPage("https://google.com")
	now = time.time()

	content1 = webpage.content
	time_taken = time.time() - now
	print(time_taken)

	now = time.time()
	content2 = webpage.content
	time_taken = time.time() - now
	print(time_taken)
	print(content2 == content1)
