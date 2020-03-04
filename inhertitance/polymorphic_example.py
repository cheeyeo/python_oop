class MediaPlayer:
	def play_audio(self, audio_file):
		audio_file.play()

class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")

		self.filename = filename

class MP3File(AudioFile):
	ext = "mp3"

	def play(self):
		print("Playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
	ext = "wav"

	def play(self):
		print("Playing {} as wav".format(self.filename))

class OggFile(AudioFile):
	ext = "ogg"

	def play(self):
		print("Playing {} as ogg".format(self.filename))

# Example of class which uses the same interface of a play method but not inheriting from AudioFile
class FlacFile:
	def __init__(self, filename):
		if not filename.endswith(".flac"):
			raise Exception("Invalid file format!")

		self.filename = filename

	def play(self):
		print("Playing {} as flac".format(self.filename))

if __name__ == "__main__":
	ogg = OggFile("myfile.ogg")
	ogg.play()

	mp3 = MP3File("myfile.mp3")
	mp3.play()

	try:
		wrong_file = MP3File("myfile.ogg")
	except Exception as e:
		print(e)

	mp = MediaPlayer()
	mp.play_audio(ogg)

	flac = FlacFile("myflac.flac")
	mp.play_audio(flac)