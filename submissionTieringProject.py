#!/usr/local/bin/python3
#Objective is to Tier accounts based on predefined identifiable categories. 
#Author:  Chris Cirelli
#Method with a loop + True function
#Create points for each category and then weights for each descriptive factor or sub factor.  So maybe industry as a whole is worth 50% of the ranking and then within that you have weights for each Tier. 

##############        BEGIN          ###########

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


##CATEGORY 1: INDUSTRIES
def readIndustry():
	Industry_Tier = {
		'TierI':   ('Retail', 'Manufacturing', 'Agriculture'),
		'TierII':  ('Construction', 'Information Tech', 'Consulting', 'Mining'),
		'TierIII': ('Biotech', 'Retail', 'Agricultural', 'Debt Collection'),
		'TierIV':  ('Financial Institution', 'Staffing Firms', 'Govt Entities')
	}
	
	#Industry Tier Weigths
	Industry_Weigth_TierI = 1
	Industry_Weigth_TierII = 0.8
	Industry_Weigth_TierIII = 0.5
	Industry_Weight_TierIV = 0.0
	
	printTiers(Industry_Tier)
	Industry = input('Industry:  ')

	if Industry in Industry_Tier['TierI']:
		I = Industry_Weigth_TierI
	elif Industry in Industry_Tier['TierII']:
		I = Industry_Weigth_TierII
	elif Industry in Industry_Tier['TierIII']:
		I = Industry_Weigth_TierIII
	elif Industry in Industry_Tier["TierIV"]:
		I = Industry_Weight_TierIV
	else:
		I = 'Industry not found.  Try again'

	return I

##CATEGORY #2: BROKERAGE FIRM
def readBrokerageFirm():
	Broker_Tier= {
		'TierI':   ('AON', 'Marsh', 'Willis', 'Lockton'),
		'TierII':  ('Wholesaler', 'Regional', 'Large Retailer'),
		'TierIII': ('Small retailer', 'Small Wholesaler')
	}
					
	#Broker Tier Weights
	Broker_TierI_weight = 1
	Broker_TierII_weight= .7
	Broker_TierIII_weight = .5
	
	printTiers(Broker_Tier)
	Broker = input('Broker:  ')

	if Broker in Broker_Tier['TierI']:
		B = Broker_TierI_weight
	elif Broker in Broker_Tier['TierII']:
		B = Broker_TierII_weight
	elif Broker in Broker_Tier['TierIII']:
		B= Broker_TierIII_weight
	else:
		B = 'Broker not found. Try again'
	
	return B

##CATEGORY 3: EMPLOYEE COUNT
def readEmplyeeCount():
	EmployeeCount_Small_weight = 0.25
	EmployeeCount_Medium_weight = 0.50
	EmployeeCount_Large_weight = 0.10
	EmployeeCount_Massive_weight = 0.75

	EmployeeCount = input('Employee Count:   ')

	if int(EmployeeCount) < 100:
		E = EmployeeCount_Small_weight
	elif int(EmployeeCount) == 100:
		E = EmployeeCount_Small_weight
	elif int(EmployeeCount) > 101 and int(EmployeeCount) < 400:
		E = EmployeeCount_Medium_weight
	elif int(EmployeeCount) == 400:
		E = EmployeeCount_Medium_weight
	elif int(EmployeeCount) > 401 and int(EmployeeCount) < 2500:
		E = EmployeeCount_Large_weight
	elif int(EmployeeCount) == 2500:
		E = EmployeeCount_Large_weight
	else:
		E = EmployeeCount_Massive_weight

	return E

## CATEGORY 4: REVENUES
def readRevenues():
	Revenues_Small_weight = 0.0
	Revenues_Medium_weight = 0.25
	Revenues_Large_weight = 0.75
	Revenues_Massive_weight = 1.0

	Revenues = input('Revenues:   ')
	if int(Revenues) < 10000000:
		R = Revenues_Small_weight
	elif int(EmployeeCount) == 10000000:
		R = Revenues_Small_weight
	elif int(Revenues) > 10000001 and int(Revenues) < 100000000:
		R = Revenues_Medium_weight
	elif int(Revenues) == 100000000:
		R = Revenues_Medium_weight
	elif int(Revenues) > 100000001 and int(Revenues) < 250000000:
		R = Revenues_Large_weight
	elif int(Revenues) == 250000000:
		R = Revenues_Large_weight
	else:
		R = EmployeeCount_Massive_weight

	return R

l = (
	(readIndustry, 'Industry factor:\n\t'),
	(readBrokerageFirm, 'Broker Factor:\n\t'),
	(readEmplyeeCount, 'Employee Count Factor:\n\t'),
	(readRevenues, 'Revenue Size Factor:n\t')
)

# SUMMARY OF FACTORS
def getInfo():
	print("\nSummary of Weights\n------------------\n")
	for t in l:
		v = t[0]()
		print(t[1], v)

c = input('Evaluate summary info (y/n)?: ')
while c != 'n':
	getInfo()
	c = input('Evaluate summary info (y/n)?: ')
