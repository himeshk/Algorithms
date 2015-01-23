import globfunct

#def createHeap(heapArray, minmax):
#	print "hi"	


def heapSort(heapArray , normal):
	lstSorted = []
	i = 0 
	heapArray = createHeap(heapArray  , normal)
	for i in range(0,len(heapArray)):
		lstSorted.append(heapArray[0])
		#print " Lst sorted"
		#globfunct.printlist(lstSorted)
		heapArray = removeFromHeap(heapArray , 0 , normal)
		#print "after removing"
		#globfunct.printlist(heapArray)
		
	return lstSorted	

def addToHeap(heapArray , minHeap):
	odd = False
	#print "len of heap " , len(heapArray)
	if (len(heapArray)) % 2 == 1:
		odd = True
	if odd == True:
		n = len(heapArray) - 1
	else:
		n = len(heapArray)
	valueOfAddedElement = heapArray[len(heapArray)-1]
	#print "value of n" , n
	while(True):
		#globfunct.printlist(heapArray)
		#print "value of n" , n
		if minHeap:
			if valueOfAddedElement < heapArray[(n/2) - 1]:			
				if odd == True: 
				#	print " in odd true begin"
				#	globfunct.printlist(heapArray)
					heapArray[n] , heapArray[(n/2)-1] = heapArray[(n/2) - 1] , heapArray[n]
				#	print " in odd true "
				#	globfunct.printlist(heapArray)
				else:
				#	print " in odd false begin "
				#	globfunct.printlist(heapArray)
					heapArray[n - 1] , heapArray[(n/2) - 1] = heapArray[(n/2) - 1] , heapArray[n - 1]
				#	print " in odd false "
				#	globfunct.printlist(heapArray)
			else:
				break
		else:
			if valueOfAddedElement > heapArray[(n/2) - 1]:			
				if odd == True: 
					heapArray[n] , heapArray[(n/2)-1] = heapArray[(n/2) - 1] , heapArray[n]
				else:
					heapArray[n - 1] , heapArray[(n/2) - 1] = heapArray[(n/2) - 1] , heapArray[n - 1]
			else:
				break

		if n == 0 or n == 1:
			break
		n = n/2
		if n == 0 or n == 1:
			break
		odd = False
		#valueOfAddedElement = heapArray[n - 1]
		if n%2 == 1: 
			n = n - 1
			odd = True
	#globfunct.printlist(heapArray)			
	return heapArray


def createHeap(heapArray , minHeap):
	lstMakeHeap = []
	i = 0 
	for i in range(0,len(heapArray)):
		lstMakeHeap.append(heapArray[i])
		lstMakeHeap = addToHeap(lstMakeHeap , minHeap)
	return lstMakeHeap	
	


#https://www.youtube.com/watch?v=ijfPvX2qYOQ
"""
in this we have used the regular method where we exchange 
the first and the last element and then and then simply 
remove the last elment and then heapify it. The reason for
(n+1)*2 is that since n is the index the formula for children 
2n and 2n+1 applies from the position 1 and not zero hence we
do +1 and then subtract 1 at then end of the operation to 
get the real index position in it.
"""

def removeFromHeap(heapArray , index , minHeap):
	odd = False
	if len(heapArray) < 1:
		return heapArray
	n = index
	"""
	if (((n+1)*2)-1) > len(heapArray):
		del heapArray[n]
		return heapArray
	"""
	heapArray[n] , heapArray[len(heapArray) - 1] =  heapArray[len(heapArray) - 1] , heapArray[n] 
	#print len(heapArray)
	del heapArray[len(heapArray) - 1]
	#print len(heapArray)
	while (((n+1)*2)-1) <= (len(heapArray) - 1):
		#globfunct.printlist(heapArray)
		#print "value of n " , ((n+1)*2)-1
		if minHeap:
			if (((n+1)*2)) <= (len(heapArray) - 1):
				#globfunct.printlist(heapArray)
				#print "value of n in if" , ((n+1)*2)-1
				if (heapArray[((n+1)*2)-1] < heapArray[((n+1)*2)-1+1]) and (heapArray[((n+1)*2)-1]  < heapArray[n]):
					heapArray[n] , heapArray[((n+1)*2)-1] = heapArray[((n+1)*2)-1] , heapArray[n]
					n = ((n+1)*2) - 1
				elif (heapArray[((n+1)*2)-1] >= heapArray[((n+1)*2)-1+1]) and (heapArray[((n+1)*2)]  < heapArray[n]):
					heapArray[n] , heapArray[((n+1)*2)-1+1] = heapArray[((n+1)*2)-1+1] , heapArray[n]
					n = ((n+1)*2) + 1 - 1
				else:
				#	print "Broke"
					break
			elif (heapArray[((n+1)*2)-1]  < heapArray[n]):
				heapArray[n] , heapArray[((n+1)*2)-1] = heapArray[((n+1)*2)-1] , heapArray[n]
				n = ((n+1)*2)-1
			else:
				break
		else:
			if (((n+1)*2)) <= (len(heapArray) - 1):
				if (heapArray[((n+1)*2)-1] > heapArray[((n+1)*2)-1+1]) and (heapArray[((n+1)*2)-1]  > heapArray[n]):
					heapArray[n] , heapArray[((n+1)*2)-1] = heapArray[((n+1)*2)-1] , heapArray[n]
					n = ((n+1)*2) - 1
				elif (heapArray[((n+1)*2)-1] <= heapArray[((n+1)*2)-1+1]) and (heapArray[((n+1)*2)]  > heapArray[n]):
					heapArray[n] , heapArray[((n+1)*2)-1+1] = heapArray[((n+1)*2)-1+1] , heapArray[n]
					n = ((n+1)*2) + 1 - 1
				else:
					break
			elif (heapArray[((n+1)*2)-1]  > heapArray[n]):
				heapArray[n] , heapArray[((n+1)*2)-1] = heapArray[((n+1)*2)-1] , heapArray[n]
				n = ((n+1)*2)-1
			else:
				break

	#del heapArray[n]
	return heapArray			
	
def main():
	lst = []
	for i in range(10):
		lst.append(i)
		#lst = addToHeap(lst , False)
		#globfunct.printlist(lst)
	#globfunct.printlist(lst)	
	#removeFromHeap(lst , 0 , True)
	#globfunct.printlist(lst)
	lst = heapSort(lst , False)
	globfunct.printlist(lst)
#main()


