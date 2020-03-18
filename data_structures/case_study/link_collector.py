from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
from queue import Queue

LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinkCollector:
	def __init__(self, url):
		parsedurl = urlparse(url)
		self.url = "{}://{}".format(parsedurl.scheme, parsedurl.netloc)
		self.collected_links = {}
		self.visited_links = set()

	def collect_links(self, path="/"):
		full_url = self.url + path
		self.visited_links.add(full_url)

		# rescue not found error
		try: 
			page = str(urlopen(full_url).read())
		except HTTPError:
			page = ""

		links = LINK_REGEX.findall(page)
		links = {self.normalize_url(path, link) for link in links}
		self.collected_links[full_url] = links
		for link in links:
			self.collected_links.setdefault(link, set())

		unvisited_links = links.difference(self.visited_links)

		for link in unvisited_links:
			if link.startswith(self.url):
				self.collect_links(urlparse(link).path)

	def collect_links_with_queue(self):
		queue = Queue()
		queue.put(self.url)
		while not queue.empty():
			url = queue.get().rstrip('/')
			self.visited_links.add(url)
			# rescue not found error
			try: 
				page = str(urlopen(url).read())
			except HTTPError:
				page = ""

			links = LINK_REGEX.findall(page)
			links = {self.normalize_url(urlparse(url).path, link) for link in links}
			# add set to collected_links dict
			self.collected_links[url] = links
			for link in links:
				self.collected_links.setdefault(link, set())
			unvisited_links = links.difference(self.visited_links)
			# print("UNVISITED: ", unvisited_links)
			for link in unvisited_links:
				if link.startswith(self.url):
					queue.put(link)


	def normalize_url(self, path, link):
		if link.startswith("http://"):
			return link
		elif link.startswith("/"):
			return self.url + link
		else:
			return self.url + path.rpartition('/')[0] + '/' + link

if __name__ == "__main__":
	collector = LinkCollector(sys.argv[1])
	collector.collect_links_with_queue()
	for link, item in collector.collected_links.items():
		print(link, item)