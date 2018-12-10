tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	colWidths = [0] * len(table)
	for i in range(len(table)):
		for j in range(len(table[i])):
			if colWidths[i] < len(table[i][j]):
				colWidths[i] = len(table[i][j])
	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = table[i][j].rjust(colWidths[i])
	fixedList = []
	for i in range(len(table[0])):
		fixedList.append([item[i] for item in table])
	for i in range(len(fixedList)):
		for j in range(len(fixedList[i])):
			print(fixedList[i][j] + " ", end='')
		print("\n")

printTable(tableData)
