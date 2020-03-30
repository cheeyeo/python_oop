import sys

class WarningFilter:
	def __init__(self, insequence):
		self.insequence = insequence

	def __iter__(self):
		return self

	def __next__(self):
		l = self.insequence.readline()
		while l and "WARNING" not in l:
			l = self.insequence.readline()
		if not l:
			raise StopIteration()
		return l.replace("\tWARNING", "")

inname = sys.argv[1]
outname = sys.argv[2]

with open(inname) as f:
	filter = WarningFilter(f)
	for l in filter:
		outname.write(l)