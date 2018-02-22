#any sorting algorithem based on comparison must do comparison by Ω(nlgn) times.
#countSort can break the limit.
#the time complexity of countSort is θ(n)
def countSort(arr,k):
    result=[None for i in range(0,len(arr)+1)]
    #temporary storage room 
    temp=[0 for i in range(0,k+1)]
    #store the number equal to arr[i]
    for i in range(0,len(arr)):
        temp[arr[i]]+=1
    #store the number <=arr[i]
    for i in range(1,k+1):
        temp[i]=temp[i]+temp[i-1]
    for j in range(len(arr)-1,-1,-1):
        result[temp[arr[j]]]=arr[j]
        temp[arr[j]]-=1
    result.remove(None)
    return result

#unittest
import unittest
from random import randint
from utils import time_decorator
class TestInsertSort(unittest.TestCase):
    #test for countSort
    def test_countSort(self):
        print("countSort's maxnumber:50")
        print('before countSort:')
        arr = [randint(1,10) for i in range(20)]
        print(arr)
        print('after countSort:')
        result = countSort(arr,10)
        print(result)
        print('countSort logical test successfully')

if __name__ == '__main__':
    unittest.main()



