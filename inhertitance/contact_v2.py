# Example of passing args to parent subclasses using multiple inheritance

class Contact:
	all_contacts = []

	def __init__(self, name="", email="", **kwargs):
		print("kwargs in Contact: ", kwargs)
		super().__init__(**kwargs)
		self.name = name
		self.email = email
		self.all_contacts.append(self)

class AddressHolder:
	def __init__(self, street="", city="", state="", code="", **kwargs):
		print("kwargs in AddressHolder: ", kwargs)
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code

class Friend(Contact, AddressHolder):
	def __init__(self, phone="", **kwargs):
		print("KWARGS in Friend class: ", kwargs)
		super().__init__(**kwargs)
		self.phone = phone

if __name__ == "__main__":
	f = Friend(phone="123456", street="Sesame Street", name="A Friend")
	print(f.name)
	print(f.phone)
	print(f.street, f.city, f.state, f.code)
	print(f.all_contacts)