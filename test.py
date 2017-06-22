#!/usr/local/bin/python3

def maxLength(a):
	maxLen = -1
	for str in a:
		if len(str) > maxLen:
			maxLen = len(str)
	return maxLen

def printTiers(tier):
	maxValueLen = []
	[maxValueLen.extend(x) for x in (row for row in tier.values())]
	maxValueLen = maxLength(maxValueLen)

	maxRowLength = 0
	for t in tier.values():
		if len(t) > maxRowLength:
			maxRowLength = len(t)
	
	totalColumns = len(tier.keys())
	totalRows = maxRowLength + 1
	table = [None] * (totalColumns * totalRows)
	
	c = 0
	r = 0
	for columnName in tier:
		pos = r*(totalColumns) + c
		table[pos] = columnName
		r += 1
		for v in tier[columnName]:
			pos = r*(totalColumns) + c
			table[pos] = v
			r += 1
		c += 1
		r = 0
	
	def padString(maxLength, str):
		return str + (' ' * (maxLength - len(str)))
	
	def getRowString(r):
		if( r == 0 ):
			return padString(maxValueLen, '')
		else:
			return padString(maxValueLen, str(r))

	dividerLine =  '-' * ((maxValueLen * (totalColumns + 1)) + ((totalColumns+1)*3) + 2)
	for r in range(totalRows):
		print(dividerLine);
		row = [getRowString(r)]
		for c in range(totalColumns):
			pos = r*totalColumns + c
			cellValue = ' ' if table[pos] == None else table[pos];
			cellValue = padString(maxValueLen, cellValue)
			row.append(cellValue)
		print('| ', ' | '.join(row), ' |')
	print(dividerLine);

Industry_Tier = {
	'TierI':   ('Retail', 'Manufacturing', 'Agriculture'),
	'TierII':  ('Construction', 'Information Tech', 'Consulting', 'Mining'),
	'TierIII': ('Biotech', 'Retail', 'Agricultural', 'Debt Collection'),
	'TierIV':  ('Financial Institution', 'Staffing Firms', 'Govt Entities')
}

printTiers(Industry_Tier)

# [__,__,__,__]
# [__,__,__,__]
# [__,__,__,__]
# [__,__,__,__]
