import re

def checkIfStrong(password):
	numRegex = re.compile(r"\d")
	numCheck = numRegex.search(password)
	lowerRegex = re.compile(r"[a-z]")
	lowerCheck = lowerRegex.search(password)
	upperRegex = re.compile(r"[A-Z]")
	upperCheck = upperRegex.search(password)
	if upperCheck == None or lowerCheck == None or numCheck == None or len(password) < 8:
		print("The password is not secure. Remember, you need at least eight characters, one digit, and a mixture of uppercase and lowercase characters.\n")
		return 0
	else:
		print("The password is secure.\n")
		return 1

check = 0

while check == 0:
	password = input("Provide a password to check for strength: ")
	check = checkIfStrong(password)