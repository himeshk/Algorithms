import sys
import time
import globfunct

def radixSort(radArray):
	reachedLastElement = True
	indexOfPosition = 1
	tempArr1 = []

	for loop2 in range(0,11):
		tempArr1.append([])
		#tempArr1.append([])
	loop1 = 0
	for loop1 in range(len(radArray)):
		tempArr1[0].append(radArray[loop1])
	#tempArr2 = tempArr1		
	while (reachedLastElement):
		reachedLastElement = False
		indexOfPosition = indexOfPosition * 10
		"""
		tempArr1 = tempArr2
		#print "Temp Arr1 new " 
		#printMultiDimenArray(tempArr1 , 2)
		"""
		"""
		del tempArr2
		tempArr2 = []
		for loop2 in range(0,10):
			tempArr2.append([])
		"""
		#i = 10
		#for i in range(10 , -1 ,-1):
		i = 0
		for i in range(11):
			loop1 = 0 
			#print i , loop1
			lengthOfArray = len(tempArr1[i]) - 1
			loop1 = lengthOfArray
			for loop1 in range(loop1 , -1 , -1):
			
				#printMultiDimenArray(tempArr1 , 2)
				if ((tempArr1[i][loop1])/indexOfPosition ) > 0:
					reachedLastElement = True
				remainder = ((tempArr1[i][loop1]%indexOfPosition)*10)/indexOfPosition 
				"""
				print "loop1 i" , loop1 , i
				print "tempArray " , tempArr1[i][loop1]
				print "remainder " , remainder
				"""
				
				if remainder > i:
					#print tempArr2[remainder]
					tempArr1[remainder].insert(0 , tempArr1[i][loop1])
					del  tempArr1[i][loop1]		
				elif remainder < i:
					tempArr1[remainder].insert(len(tempArr1[remainder]) , tempArr1[i][loop1])
					del  tempArr1[i][loop1]
				#lengthOfArray = len(tempArr1[i])
	i = 0 
	count1 = 0
	for i in range(0,10):
		loop1 = 0
		for loop1 in range(len(tempArr1[i])):
			radArray[count1] = tempArr1[i][loop1]
			#print tempArr2[i][loop1]
			count1 = count1 + 1
	#printMultiDimenArray(tempArr1 , 2)	
	return radArray

def printMultiDimenArray(lstToPrint , numOfDimentions):
	for loop1 in range(len(lstToPrint)):
		print ""
		for loop2 in range(len(lstToPrint[loop1])):
			print lstToPrint[loop1][loop2] , " " , 
	

	
def main():
	lst = []
	lst2 = []
	sizeofList = 4
	for i in range(sizeofList):
		lst.append(sizeofList-i)
	lst.append(67)
	#globfunct.printlist(lst)
	radixSort(lst)
	globfunct.printlist(lst)	
"""
print sys.getrecursionlimit()
str_Time = time.time()
sys.setrecursionlimit(500000)
main()
print ("Time in seconds : ", time.time() - str_Time )
"""
			
			