from .zipprocessor import ZipProcessor

class ZipReplace(ZipProcessor):
	def __init__(self, filename, search_string, replace_string):
		super().__init__(filename)
		self.search_string = search_string
		self.replace_string = replace_string

	def process_files(self):
		"""perform a search and replace on all-files in temporary directory"""
		for filename in self.temp_directory.iterdir():
			with open(filename, "r") as f:
				contents = f.read()
			contents = contents.replace(self.search_string, self.replace_string)
			with open(filename, "w") as f:
				f.write(contents)