def selectSort(arr):
    length=len(arr)
    for i in range(0,length):
        select=arr[i]
        for j in range(i+1,length):
            if arr[j] < select:
                arr[i],arr[j]=arr[j],arr[i]
                select=arr[i]

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestselectSort(unittest.TestCase):
    #test for selectSort
    def test_selectSort(self):
        print('before selectSort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after selectSort:')
        selectSort(arr)
        print(arr)
        print('selectSort logical test successfully')
    #test for time performance
    def test_selectSort_time(self):
        print('test 1000 numbers')
        arr1 = [randint(1,500) for i in range(1000)]
        count1 = time_decorator(selectSort)(arr1)
        print('average time cost:',count1,'s')
        arr2 = [i for i in range(1000)]
        count2 = time_decorator(selectSort)(arr2)
        print('best time cost:',count2,'s')
        arr3 = [i for i in range(1000,-1,-1)]
        count3 = time_decorator(selectSort)(arr3)
        print('worst time cost:',count3,'s')


if __name__ == '__main__':
    unittest.main()

