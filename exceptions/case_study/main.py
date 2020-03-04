from authenticator import Authenticator
from authorizor import Authorizor

authenticator = Authenticator()
authorizor = Authorizor(authenticator)

authenticator.add_user("joe", "password")
authorizor.add_permission("paint")

authenticator.login("joe", "password")

authorizor.permit_user("paint", "joe")

print(authorizor.check_permission("paint", "joe"))