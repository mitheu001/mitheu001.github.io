import random
import string
import hashlib


def generate_password(length):
	chars = string.ascii_letters + string.digits +string.punctuation 

	password = ''.join(random.choice(chars) for i in range(length))
	return password

password = generate_password(10)
hashed_password = hashlib.sha256(password.encode()).hexdigest()


print(password, "Save your password save so that you can remember next time")



