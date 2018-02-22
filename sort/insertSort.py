def insertSort(arr):
    #the length of the arr
    length=len(arr)
    for i in range(1,length):
        #choose the number to be inserted
        insert=arr[i]
        #the initial index
        k=-1
        #search the index to be inserted
        for j in range(0,i):
            if insert<arr[j]:
                k=j
                break
        #move arr[k:i+1] to the right by one position to insert the number chosen
        if k != -1:
            for m in range(k,i+1):
                arr[m],insert=insert,arr[m]
    
#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for insertSort
    def test_InsertSort(self):
        print('before InsertSort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after InsertSort:')
        insertSort(arr)
        print(arr)
        print('InsertSort logical test successfully')
    #test for time performance
    def test_InsertSort_time(self):
        print('test 1000 numbers')
        arr1 = [randint(1,500) for i in range(1000)]
        count1 = time_decorator(insertSort)(arr1)
        print('average time cost:',count1,'s')
        arr2 = [i for i in range(1000)]
        count2 = time_decorator(insertSort)(arr2)
        print('best time cost:',count2,'s')
        arr3 = [i for i in range(1000,-1,-1)]
        count3 = time_decorator(insertSort)(arr3)
        print('worst time cost:',count3,'s')


if __name__ == '__main__':
    unittest.main()


