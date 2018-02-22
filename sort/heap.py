#the function to keep the big-heap
def max_heapify(arr,i,length):
    #2*i+1 is the left child index of i index
    if 2*i+1 < length and arr[2*i+1] > arr[i]:
        largest=2*i+1
    else:
        largest = i
    #2*i+2 is the right child index of i index
    if 2*i+2 < length and arr[2*i+2] > arr[largest]:
        largest = 2*i+2
    #if the largest node index is not i, it should be adjusted recursively
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr,largest,length)

#build a max-heap by an array
def max_heap(arr):
    length=len(arr)-1
    mid=int(length/2)
    for i in range(mid-1,-1,-1):
        max_heapify(arr,i,len(arr)-1)

#the main function of heapSort
def heap_sort(arr):
    max_heap(arr)
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heapify(arr,0,i-1)

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for heapSort
    def test_heapSort(self):
        print('before heapSort:')
        arr = [randint(1,50) for i in range(20)]
        print(arr)
        print('after heapSort:')
        heap_sort(arr)
        print(arr)
        print('heapSort logical test successfully')
    #test for time performance
    def test_heapSort_time(self):
        print('test 10000 numbers:')
        arr1 = [randint(1,500) for i in range(10000)]
        count1 = time_decorator(heap_sort)(arr1)
        print('average time cost:',count1,'s')
        arr2 = [i for i in range(10000)]
        count2 = time_decorator(heap_sort)(arr2)
        print('best time cost:',count2,'s')


if __name__ == '__main__':
    unittest.main()


