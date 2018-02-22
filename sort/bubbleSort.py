#bubbleSort
def BubbleSort(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(length-1,i,-1):
            #swap for the neighbours
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for bubbleSort
    def test_bubbleSort(self):
        print('before bubbleSort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after bubbleSort:')
        BubbleSort(arr)
        print(arr)
        print('bubbleSort logical test successfully')
    #test for time performance
    def test_bubbleSort_time(self):
        print('test 1000 numbers:')
        arr1 = [randint(1,500) for i in range(1000)]
        count1 = time_decorator(BubbleSort)(arr1)
        print('average time cost:',count1,'s')
        arr2 = [i for i in range(1000)]
        count2 = time_decorator(BubbleSort)(arr2)
        print('best time cost:',count2,'s')
        arr3 = [i for i in range(1000,-1,-1)]
        count3 = time_decorator(BubbleSort)(arr3)
        print('worst time cost:',count3,'s')


if __name__ == '__main__':
    unittest.main()
