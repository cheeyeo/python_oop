import sys
import re

pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
	template = "'{}' matches pattern '{}'".format(search_string, pattern)
else:
	template = "'{}' does not match pattern".format(search_string, pattern)

print(template)