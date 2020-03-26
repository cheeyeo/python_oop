class EMail():
	def __init__(self, from_addr, to_addr, subject, message):
		self.from_addr = from_addr
		self.to_addr = to_addr
		self.subject = subject
		self.__message = message

	def message(self):
		return self.__message


email = EMail("a@example.com", "b@example.com", "You have mail", "Here's some email for you")


formatted = f"""
From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: <{email.subject}>

{email.message()}"""

print(formatted)