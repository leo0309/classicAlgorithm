### A summary of classical sort algorithm

1. insertSort

   The basic idea is to insert a number  into a sorted array, like inserting a card into an ordered pile of cards.

2. selectSort

   from an array needed to be ordered to choose a number one by one, insert the number chosen into the remaining array ordered by increment.

3. bubbleSort

   It is like a bubble rising from the bottom to the top. The smaller it is, the earlier it rises. Neighbor elements swap with each other if the former is larger than the latter.

4. mergeSort

   It implements by binary recursion and the extra space is needed.

5. heapSort

   Firstly, a big-heap must be built. Because the root is the biggest element in the array, exchange the root with the tail and decrease the length of the array by 1. With the function of keeping the big-heap, the next biggest element will still be the root. With recursive calls, the array will be in order.

6. quickSort

   It is implemented by a partition. The average performance is good. However, the worst performance is O(n^2). With random means, the shortcoming can be overcome.

7. countSort

   It is not based on comparison. The performance is well. However, it will take too much space.

------

### Conclusion on complexity

| SortFunction | average   | best      | worst     | extra space | sustainability |
| ------------ | --------- | --------- | --------- | ----------- | -------------- |
| insertSort   | O(n^2)    | O(n)      | O(n^2)    | O(1)        | yes            |
| selectSort   | O(n^2)    | O(n^2)    | O(n^2)    | O(1)        | no             |
| bubbleSort   | O(n^2)    | O(n)      | O(n^2)    | O(1)        | yes            |
| mergeSort    | O(nlogn)  | O(nlogn)  | O(nlogn)  | O(n)        | yes            |
| heapSort     | O(nlogn)  | O(nlogn)  | O(nlogn)  | O(1)        | no             |
| quickSort    | O(nlogn)  | O(nlogn)  | O(n^2)    | O(1)        | yes            |
| countSort    | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n)        | yes            |

------



###经典排序方法概述

1. 插入排序(insertSort.py)

   基本思路是将一个数据插入到一组已排好序的数据集中(类似于将一张牌插入到已排好序的牌堆中)。

2. 选择排序(selectSort.py)

   从待排序的数组中依次选择一个数，将该数按从小到大的顺序插入到剩余的数组中。

3. 冒泡排序(bubbleSort.py)

   类似于冒泡过程。基于比较大小，相邻元素之间不断进行交换位置。

4. 合并排序(mergeSort.py)

   不断进行二分递归。需要设置哨兵，并且需要额外的空间。

5. 堆排序(heap.py)

   首先需要建立最大堆。由于最大堆的根节点(即'arr[0]')为整个待排序数组的最大的值，将该最大值和数组的最末尾交换(最大值移动到数组尾部），且数组长度需要减1，利用保持最大堆的性质的子过程，保持最大堆。重复上述过程，递归下去，即可实现排序。堆排序是不稳定排序。

6. 快速排序(quickSort.py)

   对于待排序数组不断进行二分划分为子过程。对子过程进行排序。不断递归调用。快速排序不占用额外空间，平均性能比较好，但如果整个数组原本就有序，则性能最差。此时可以采用随机化手段进行克服。

7. 计数排序(countSort.py)

   该方法不是基于比较来进行排序。性能很好。但是需要额外的空间。

   -------

   ### 复杂度总结

   | 排序方法 | 平均情况  | 最好情况  | 最坏情况  | 额外空间 | 稳定性 |
   | -------- | --------- | --------- | --------- | -------- | ------ |
   | 插入排序 | O(n^2)    | O(n)      | O(n^2)    | O(1)     | 稳定   |
   | 选择排序 | O(n^2)    | O(n^2)    | O(n^2)    | O(1)     | 不稳定 |
   | 冒泡排序 | O(n^2)    | O(n)      | O(n^2)    | O(1)     | 稳定   |
   | 合并排序 | O(nlogn)  | O(nlogn)  | O(nlogn)  | O(n)     | 稳定   |
   | 堆排序   | O(nlogn)  | O(nlogn)  | O(nlogn)  | O(1)     | 不稳定 |
   | 快速排序 | O(nlogn)  | O(nlogn)  | O(n^2)    | O(1)     | 稳定   |
   | 计数排序 | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n)     | 稳定   |

   ​

   ​

   ​