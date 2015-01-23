import sys
import time
import globfunct

def MergeSort(sortArr):
	#globfunct.printlist(sortArr)
	if len(sortArr) == 2:
		if sortArr[0] < sortArr[1]:
			#print sortArr[0] , " , " , sortArr[1]
			return sortArr
		else:
			#print sortArr[0] , " , " , sortArr[1]
			sortArr[0], sortArr[1] = sortArr[1], sortArr[0]
			return sortArr

	elif len(sortArr) == 1:
		return sortArr

	elif len(sortArr) == 0:
		#print "Empty Array"
		return sortArr
	else:
		lstLeft = []
		lstRight = []
		lstFinal = []
		#centerVal = sortArr[0]
		"""
		for i in range(1 , len(sortArr)):
			if sortArr[i] > sortArr[0]:
				lstLeft.append(sortArr[i])
			else:
				lstRight.append(sortArr[i])
		"""
		"""
		print "Left Array" 
		printlist(lstLeft)
		print "Right Array" 
		printlist(lstRight)
		"""
		n = len(sortArr)
		if (n-1)%2 == 1:
			n = ((n/2) - 1)			
		else:
			n = ((n-1)/2)

		#if len(lstLeft) > 0:		
		lstLeft = MergeSort(sortArr[:n])
		"""
		print "Left Array After Sort" 
		printlist(lstLeft)
		print "Right Array Sort" 
		printlist(lstRight)
		"""
		#if len(lstRight) > 0:
		lstRight = MergeSort(sortArr[n:])
		"""
		print "Left Array Sorted" 
		printlist(lstLeft)
		print "Right Array Sorted" 
		printlist(lstRight)
		"""
		#lstRight.append(centerVal)
		"""5  , 
		print "Final List"
		printlist(lstRight + lstLeft)
		"""
		rgtCount = 0 
		lftCount = 0
		while True:
			
			#globfunct.printlist(lstRight + lstLeft)
			if  lftCount < len(lstLeft) and rgtCount < len(lstRight):			
				#print lstLeft[lftCount] , " , " , lstRight[rgtCount]
				#print "In one"
				if lstRight[rgtCount] > lstLeft[lftCount]:
					lstFinal.append(lstLeft[lftCount])
					lftCount = lftCount + 1	
				else:
					lstFinal.append(lstRight[rgtCount])
					rgtCount = rgtCount + 1
			else:
				if lftCount >= len(lstLeft) and rgtCount < len(lstRight):
					lstFinal.append(lstRight[rgtCount])
					rgtCount = rgtCount + 1
				elif rgtCount >= len(lstRight) and lftCount < len(lstLeft):
					lstFinal.append(lstLeft[lftCount])
					lftCount = lftCount + 1	
				else:
					break

		return lstFinal
	"""
	totalLst[]
	totalLst.append(lstLeft)
	totalLst.append(centerVal)
	totalLst.append(lstRight)
	"""

def main():
	lst = []
	sizeofList = 5
	for i in range(sizeofList):
		lst.append(sizeofList-i)
	#globfunct.printlist(lst)
	lst = MergeSort(lst)
	globfunct.printlist(lst)	
"""
print sys.getrecursionlimit()
str_Time = time.time()
sys.setrecursionlimit(500000)
main()
print ("Time in seconds : ", time.time() - str_Time )
"""
#main()
