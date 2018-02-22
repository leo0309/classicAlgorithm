from random import randint

#basic partition
def partition(arr,start,end):
    if start>end:
        return
    """
    #random means
    r=randint(start,end)
    arr[r],arr[end]=arr[end],arr[r]
    """
    s=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j] <= s:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1

#Hoare partition
"""
def partition(arr,start,end):
    if start>end:
        return
    x=arr[start]
    i=start
    j=end
    while i<=end and j>=start:
        while j>=start and arr[j] >= x :
            j-=1
        while i<=end and arr[i] <= x:
            i+=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            arr[start],arr[j]=arr[j],arr[start]
            return j
"""
        

#the main function of quicksort
def quicksort(arr,start,end):
    if start < end:
        p=partition(arr,start,end)
        quicksort(arr,start,p-1)
        quicksort(arr,p+1,end)

#tail recursion quicksort
def quicksort1(arr,start,end):
    while start<end:
        p=partition(arr,start,end)
        quicksort1(arr,start,p-1)
        start=p+1

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for quicksort
    def test_quicksort(self):
        print('before quicksort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after quicksort:')
        quicksort(arr,0,len(arr)-1)
        print(arr)
        print('quicksort logical test successfully')
    #test for time performance
    def test_quicksort_time(self):
        print('test 8000 numbers:')
        arr1 = [randint(1,500) for i in range(8000)]
        count1 = time_decorator(quicksort)(arr1,0,len(arr1)-1)
        print('average time cost:',count1,'s')
        arr2 = [i for i in range(8000)]
        
        count2 = time_decorator(quicksort)(arr2,0,len(arr2)-1)
        print('worst time cost:',count2,'s')
        
        


if __name__ == '__main__':
    unittest.main()

