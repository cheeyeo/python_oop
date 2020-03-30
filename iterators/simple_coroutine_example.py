def tally():
	score = 0
	while True:
		increment = yield score
		print('INCREMENT IS: ', increment)
		score += increment


