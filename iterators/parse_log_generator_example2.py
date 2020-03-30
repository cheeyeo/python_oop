import sys

def warnings_filter(insequence):
	for l in insequence:
		if "WARNING" in l:
			yield l.replace("\tWARNING", "")


inname = sys.argv[1]
outname = sys.argv[2]

with open(inname) as infile:
	with open(outname, "w") as outfile:
		filter = warnings_filter(infile)
		for l in filter:
			outfile.write(l)