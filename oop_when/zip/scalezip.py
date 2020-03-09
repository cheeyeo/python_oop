from .zipprocessor import ZipProcessor
from PIL import Image

class ScaleZip(ZipProcessor):
	def __init__(self, filename):
		super().__init__(filename)

	def process_files(self):
		"""Scale each image in directory to 640x480"""
		for filename in self.temp_directory.iterdir():
			im = Image.open(str(filename))
			scaled = im.resize((640, 480))
			scaled.save(filename)