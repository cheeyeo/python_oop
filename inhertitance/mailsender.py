from contact import Contact

class MailSender:
	def send_mail(self, message):
		print("Sending mail to {}".format(self.email))

class EmailableContact(Contact, MailSender):
	pass

if __name__ == "__main__":
	e = EmailableContact("JOhn Smith", "john@example.com")

	print(Contact.all_contacts)

	e.send_mail("Hello, test email")