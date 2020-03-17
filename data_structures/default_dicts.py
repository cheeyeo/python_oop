from collections import defaultdict

# use defaultdict to set an intial value for an empty key in dict
# defaultdict takes a function
def letter_frequency(sentence):
	frequencies = defaultdict(int)
	for letter in sentence:
		frequencies[letter] += 1
	return frequencies

num_items = 0
def tuple_counter():
	global num_items
	num_items += 1
	return (num_items, [])

d = letter_frequency("quick brown fox")
print(d)

d = defaultdict(tuple_counter)
print(d)
d['a'][1].append('hello!')
print(d)