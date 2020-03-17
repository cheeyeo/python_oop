class Silly:
	@property
	def silly(self):
		print(self._silly)
		print("This is silly!")
		return self._silly

	@silly.setter
	def silly(self, value):
		print("You are setting {} value".format(value))
		self._silly = value

	@silly.deleter
	def silly(self):
		print("You killed silly")
		del self._silly

if __name__ == "__main__":
	s = Silly()
	# if attribute is not set, it does not exist on the object and will fail with no attribute error; similar to when you instantiate an empty class but don't define the attribute..
	s.silly = "WOAH!"
	print(s.silly)
	del s.silly

	# fail here since attribute is deleted...
	print(s.silly)