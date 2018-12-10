import re

def regexStrip(string, stripstring = None):
	if stripstring == None:
		nonWhiteSpaceRegex = re.compile(r"\S+")
		nonWhiteSpace = nonWhiteSpaceRegex.findall(string)
		for i in range(len(nonWhiteSpace)):
			print(nonWhiteSpace[i], end='')
	else:
		userStripRegex = re.compile(r"[%s]" %stripstring)
		userStrip = userStripRegex.sub('', string)
		for i in range(len(userStrip)):
			print(userStrip[i], end='')

string = input('Give something: ')
regexStrip(string, 'a')