# Inherit from built-in class dict
class LongNameDict(dict):
	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key

		return longest

if __name__ == "__main__":
	longkeys = LongNameDict()
	longkeys["hello 1"] = 1
	longkeys["longest yet"] = 5
	print(longkeys.longest_key())