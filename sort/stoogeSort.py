#stoogeSort
def stoogeSort(arr,start,end):
    if start >= end:
        return
    if arr[start]>arr[end]:
        arr[start],arr[end]=arr[end],arr[start]
    if start+1>=end:
        return
    k=int((end-start+1)/3)
    stoogeSort(arr,start,end-k)
    stoogeSort(arr,start+k,end)
    stoogeSort(arr,start,end-k)

from random import randint
from time import time
arr=[randint(1,1000) for i in range(1000)]
#arr=[i for i in range(10000)]
print(arr)
#print(arr[0:20])
tc=time()
stoogeSort(arr,0,len(arr)-1)
print(arr)
tc=time()-tc
#print(arr[0:20])
print(tc)       