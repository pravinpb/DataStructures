import time
import random

class TimeComplexity:
    def __init__(self):
        self.start_range = int(input('Enter the start range :'))
        self.end_range = int(input('Enter the end range :'))
        self.number = int(input('Number of elements :'))

    def quick_sort(self,arr) :
        if len(arr) <= 1:
            return arr
        else :
            pivot = arr.pop()
        greater_list = []
        lesser_list = []

        for ele in arr :
            if ele > pivot :
                greater_list.append(ele)
            else :
                lesser_list.append(ele)
        return self.quick_sort(lesser_list) + [pivot] + self.quick_sort(greater_list)

    def mergesort(self,arr):
        n = len(arr)

        if n <= 1:
            return arr
        else:
            mid = n // 2
            left, right = arr[:mid], arr[mid:]

            self.mergesort(left);self.mergesort(right)

            l = r = k = 0

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    arr[k] = left[l]
                    l += 1
                else:
                    arr[k] = right[r]
                    r += 1
                k += 1

            while l < len(left):
                arr[k] = left[l]
                l += 1
                k += 1

            while r < len(right):
                arr[k] = right[r]
                r += 1
                k += 1

    def execution_time(self):
        self.func = input('MergeSort or QuickSort (M / Q) :').lower()
        lis = [random.randint(self.start_range,self.end_range) for _ in range(self.number)]
        if self.func == 'q':
            st = time.time()
            self.quick_sort(lis)
            et = time.time()
            return (et-st)*1000

        elif self.func == 'm':
            st = time.time()
            self.mergesort(lis)
            et = time.time()
            return (et-st)*1000

        else:
            return 'Invalid Choice'

exec_time = TimeComplexity()
p = exec_time.execution_time()
print(p)