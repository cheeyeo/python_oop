import json
from json import JSONEncoder as JSONEncoder

class Contact:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def full_name(self):
		return "{} {}".format(self.first, self.last)

class ContactEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Contact):
			return {
			  "is_contact": True,
			  "first": obj.first,
			  "last": obj.last,
			  "full": obj.full_name
			}

		return super().default(obj)

def decode_contact(dic):
	if dic.get("is_contact"):
		return Contact(dic["first"], dic["last"])
	else:
		return dic

c = Contact("John", "SMITH")
json_encoded = json.dumps(c, cls=ContactEncoder)
print("Encoded: ", json_encoded)

c = json.loads(json_encoded, object_hook=decode_contact)
print("Decoded: ", c.__dict__)
print(c.full_name)