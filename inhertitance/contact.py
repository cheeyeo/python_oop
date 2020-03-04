class ContactList(list):
	def search(self, name):
		"""
		return all contacts that match name
		"""
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts


class Contact:
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)

class Supplier(Contact):
	def order(self, order):
		print("Sending order {} to {}".format(order, self.name))

class AddressHolder:
	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code

class Friend(Contact, AddressHolder):
	def __init__(self, name, email, phone, street, city, state, code):
		Contact.__init__(self, name, email)
		AddressHolder.__init__(self, street, city, state, code)
		self.phone = phone

if __name__ == "__main__":
	# c = Contact("somebody", "somebody@example.com")
	# s = Supplier("supplier", "supplier@example.com")

	# print(c.all_contacts)

	# print(s.order("pliers"))

	# assert c.order("pliers"), "AttributeError"

	c1 = Contact("John A", "johna@example.com")
	c2 = Contact("John B", "johnb@example.com")
	c3 = Contact("Jenna C", "jennac@example.com")
	print(Contact.all_contacts)
	print([c.name for c in Contact.all_contacts.search("John")])