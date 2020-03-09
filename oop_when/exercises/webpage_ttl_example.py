# Example of using a cache with TTL
# Returns cache only if its requested before timeout expired

import time
from urllib.request import urlopen

class WebPage:
	def __init__(self, url, ttl=1):
		self.url = url
		self._content = None
		self.ttl = ttl
		self.expires_at = time.time() + self.ttl
		self._expired = False

	def expired(self):
		if self._expired is False:
			return (self.expires_at < time.time())
		else:
			return self._expired

	@property
	def content(self):
		print("Fetching content....")

		if not self._content or self.expired():
			print("Retrieving web page...")
			self._content = urlopen(self.url).read()
			self._expired = False
			self.expires_at = time.time() + self.ttl

		return self._content

if __name__ == "__main__":
	wp = WebPage("https://google.com", ttl=10)
	content = wp.content

	time.sleep(11)
	content = wp.content

	time.sleep(2)
	content = wp.content
	print(content)
