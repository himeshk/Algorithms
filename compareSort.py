import HeapDataStructure
import QuickSort
import globfunct
import random
import time
import sys
import bubble
import MergeSort
import Radix

lstCheck = []
for i in range(500000):
       #lstCheck.append(5000-i)	
	lstCheck.append(random.randrange(-10000000,10000000))
lstCheck2 = lstCheck
lstCheck3 = lstCheck
sys.setrecursionlimit(10000000)

"""
str_Time = time.time()
#sys.setrecursionlimit(500000)
#globfunct.printlist(HeapDataStructure.heapSort(lstCheck2 , True))
HeapDataStructure.heapSort(lstCheck2 , True)
print ("By Heap Time in seconds : ", time.time() - str_Time )
"""
str_Time = time.time()
#globfunct.printlist(QuickSort.QuickSort(lstCheck))
Radix.radixSort(lstCheck)
print ("By Radix Time in seconds : ", time.time() - str_Time )

str_Time = time.time()
#globfunct.printlist(QuickSort.QuickSort(lstCheck))
QuickSort.QuickSort(lstCheck2)
print ("By Quick Time in seconds : ", time.time() - str_Time )

str_Time = time.time()
#sys.setrecursionlimit(500000)
#globfunct.printlist(MergeSort.MergeSort(lstCheck3))
MergeSort.MergeSort(lstCheck3)
print ("By Merge Time in seconds : ", time.time() - str_Time )

"""
str_Time = time.time()
#sys.setrecursionlimit(500000)
bubble.bubbleSort(lstCheck3)
print ("By Bubble Time in seconds : ", time.time() - str_Time )
"""
