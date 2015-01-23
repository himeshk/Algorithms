"""
print "This line will be printed."
int1 = 10
flt1 = float(10.23)
str1 = "hiii"

print "Str %s"  % str1 
print " int1 %f"  % flt1 
print  " flt1 %d"  % int1

mynums = [12,3,5,3,76,8,54]
"""
def bubbleSort(mynums):
	for i in range(len(mynums)):
		for z in range(len(mynums) - 1 - i):
			if mynums[z] > mynums[z+1]:
						mynums[z] , mynums[z+1] = mynums[z+1] , mynums[z]
	
	return mynums
#print (mynums)