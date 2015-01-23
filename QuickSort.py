import sys
import time
import globfunct
def QuickSort(sortArr):
	#printlist(sortArr)
	if len(sortArr) == 2:
		if sortArr[0] < sortArr[1]: 
			return sortArr
		else:
			sortArr[0], sortArr[1] = sortArr[1], sortArr[0]
			return sortArr

	elif len(sortArr) == 1:
		return sortArr

	elif len(sortArr) == 0:
		print "Empty Array"
		return sortArr
	else:
		lstLeft = []
		lstRight = []
		centerVal = sortArr[0]
		for i in range(1 , len(sortArr)):
			if sortArr[i] > sortArr[0]:
				lstLeft.append(sortArr[i])
			else:
				lstRight.append(sortArr[i])
		"""
		print "Left Array" 
		printlist(lstLeft)
		print "Right Array" 
		printlist(lstRight)
		"""
		if len(lstLeft) > 0:		
			lstLeft = QuickSort(lstLeft)
		"""
		print "Left Array After Sort" 
		printlist(lstLeft)
		print "Right Array Sort" 
		printlist(lstRight)
		"""
		if len(lstRight) > 0:
			lstRight = QuickSort(lstRight)
		"""
		print "Left Array Sorted" 
		printlist(lstLeft)
		print "Right Array Sorted" 
		printlist(lstRight)
		"""
		lstRight.append(centerVal)
		"""
		print "Final List"
		printlist(lstRight + lstLeft)
		"""
		return lstRight + lstLeft
	"""
	totalLst[]
	totalLst.append(lstLeft)
	totalLst.append(centerVal)
	totalLst.append(lstRight)
	"""

def main():
	lst = []
	sizeofList = 10
	for i in range(sizeofList):
		lst.append(sizeofList-i)
	#globfunct.printlist(lst)
	lst = QuickSort(lst)
	globfunct.printlist(lst)	
"""
print sys.getrecursionlimit()
str_Time = time.time()
sys.setrecursionlimit(500000)
main()
print ("Time in seconds : ", time.time() - str_Time )
"""
