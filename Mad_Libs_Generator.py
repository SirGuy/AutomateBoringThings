madLibFile = open('C:\\Users\\Ben\\Desktop\\PythonProjects\\Mad_Lib_Content.txt')
madLibContent = madLibFile.read()
madLibFile.close()
print(madLibContent + "\n")
madLibContent = madLibContent.split()

def replaceWords(string, word):
	for i in range(len(string)):
		if string[i] == word:
			replacement = input("Provide a replacement " + word.lower() + ": ")
			string[i] = replacement
	return string

fixedstring = replaceWords(madLibContent, "ADJECTIVE")
fixedstring = replaceWords(fixedstring, "NOUN")
fixedstring = replaceWords(fixedstring, "VERB")

for i in range(len(fixedstring)):
	print(fixedstring[i] + ' ', end='')

madLibPort = open("Mad_Lib_Filled.txt", "w")
for i in range(len(fixedstring)):
	madLibPort.write(fixedstring[i] + ' ')