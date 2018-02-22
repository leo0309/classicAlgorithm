from copy import deepcopy
from sys import maxsize
#the merge process
def merge(arr,start,mid,end):
    if start>end:
        return 
    #deep-copy
    left=deepcopy(arr[start:mid+1])
    #append the guard on the both ends
    left.append(maxsize)
    right=deepcopy(arr[mid+1:end+1])
    right.append(maxsize)
    i=j=0
    for k in range(start,end+1):
        if left[i] != maxsize or right[j] != maxsize:
            if left[i] <= right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1

#the main function of mergeSort
def mergeSort(arr,start,end):
    if start<end:
        mid=int((start+end)/2)
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for mergeSort
    def test_mergeSort(self):
        print('before mergeSort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after mergeSort:')
        mergeSort(arr,0,len(arr)-1)
        print(arr)
        print('mergeSort logical test successfully')
    #test for time performance
    def test_mergeSort_time(self):
        arr1 = [randint(1,500) for i in range(10000)]
        count1 = time_decorator(mergeSort)(arr1,0,len(arr1)-1)
        print('average time cost:',count1,'s')


if __name__ == '__main__':
    unittest.main()


