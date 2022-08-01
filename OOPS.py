'''Expirement 1'''



# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         a = round(3.14*self.r**2)
#         return f'The area is :{a} {u} sqr'
#     def circumfrence(self):
#         c = round(2*3.14*self.r)
#         return f'The circumfrence is :{c} {u}'

# r = int(input('Enter radious :'))
# u = input('Units :')
# obj = Circle(r)
# x = obj.area()
# y = obj.circumfrence()
# print(x)
# print(y)


# class CharDiv:
#     def __init__(self,strings,k):
#         self.strings = strings
#         self.k = k 
#     def multiple(self):
#         for i in range(1, len(self.strings)):
#             if 1 % self.k == 0:
#                 print(f'The character in index is divisible by k is {self.strings[i-1]}')

# k = int(input("Enter the number for which the index of multiples should be returned :"))
# strings = input('Enter a string :')
# obj = CharDiv(strings,k)
# obj.multiple()


# '''Stack'''

# from os import remove


# class StackOverflowError(Exception):
#     pass

# class StackUnderflowError(Exception):
#     pass


# class Stack():

#     def __init__(self):
#         self.stacks = []
#         self.length = int(input('length of your Stack :'))
    
#     def push(self,x):
#         if len(self.stacks) >= self.length:
#             raise StackOverflowError

#         self.stacks.append(x)
#         print(self.stacks)

    
#     def pop(self):
#         if len(self.stacks) <= 0:
#             raise StackUnderflowError

#         self.stacks.pop()
#         print(self.stacks)


# stack = Stack()

# exit = False
# while exit == False:
#     q = input('Enter the operation you have to do [push,pop,exit] :')
#     if q == 'push':
#         f = input('enter the element to be pushed :')
#         stack.push(f)
#     elif q == 'pop':
#         stack.pop()
#     elif q == 'exit':
#         exit = True


# '''Queue'''

# class QueueOverflowError(Exception):
#     pass

# class QueueUnderflowError(Exception):
#     pass


# class Queue():

#     def __init__(self):
#         self.queues = []
#         self.length = int(input('length of your Queue :'))
    
#     def enqueue(self,x):
#         if len(self.queues) >= self.length:
#             raise QueueOverflowError

#         self.queues.append(x)
#         print(self.queues)

    
#     def dequeue(self):
#         if len(self.queues) <= 0:
#             raise QueueUnderflowError

#         self.queues.pop(0)
#         print(self.queues)


# queue = Queue()

# exit = False
# while exit == False:
#     q = input('Enter the operation you have to do [enqueue,dequeue,exit] :')
#     if q == 'enqueue':
#         f = input('enter the element to be pushed :')
#         queue.enqueue(f)
#     elif q == 'dequeue':
#         queue.dequeue()
#     elif q == 'exit':
#         exti = True


# '''Sorting'''
# '''Bubble Sort'''

# def BubbleSort(list_input):
#     n = len(list_input)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list_input[j] > list_input[j+1]:
#                 list_input[j],list_input[j+1] = list_input[j+1],list_input[j]
#             print(list_input)

# BubbleSort([98,87,76,76,65,54])

# '''Selection Sort'''

# def SelectionSort(list_input):
#     n = len(list_input)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1,n):
#             if list_input[min_index] > list_input[j]:
#                 min_index = j 

#         list_input[i] , list_input[min_index] = list_input[min_index] , list_input[i]
#     print(list_input)

# SelectionSort([98,87,76,76,65,54])

# '''Insertion Sort'''

# def InsertionSort(list_input):
#     n = len(list_input)
#     for i in range(1,n):
#         key = list_input[i]

#         j = i-1
#         while j>=0 and key < list_input[j]:
#             list_input[j+1] = list_input[j]
#             j = j-1
#         list_input[j+1] = key
#         print(list_input)

# InsertionSort([98,87,76,76,65,54])

# '''Quick Sort'''
# def quick_sort(arr) :
#     if len(arr) <= 1:
#         return arr
#     else :
#         pivot = arr.pop()
#     greater_list = []
#     lesser_list = []

#     for ele in arr :
#         if ele > pivot :
#             greater_list.append(ele)
#         else :
#             lesser_list.append(ele)
#     return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)

# print(quick_sort([12,34,1,2,63,98,43]))

# ''' insertion sort '''

# def insertion_sort(arr) :
#     for i in range(1,len(arr)) :
#         while arr[i-1] > arr[i] and i > 0 :
#             arr[i-1],arr[i] = arr[i] , arr[i-1]
#             i -= 1
#     return arr
# print(insertion_sort([2,4,3,1,4,7,9,2,1]))


''' bubble sort '''
# def bubble_sort(arr) :
#     for i in range(len(arr)) :
#         for j in range(len(arr)-i-1) :
#             if arr[j] > arr[j+1] :
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# print(bubble_sort([23,1,6,312,3,2]))        

''' selection sort '''

# def selection_sort(arr) :
#     for i in range(len(arr)) :
#         min = i
#         for j in range(i+1,len(arr)) :
#             if arr[min] > arr[j] :
#                 min = j
#         arr[i],arr[min] = arr[min],arr[i]

#     return arr
# print(selection_sort([23,123,1,3,21,2]))


''' merge sort '''


''' binary search '''

# def bianry_search(arr,ele) :
#     print(arr)
#     begin_index = 0
#     end_index = len(arr) - 1
#     while begin_index <= end_index :
#         midpoint = begin_index + (end_index - begin_index ) // 2
#         mid_value = arr[midpoint]
#         if mid_value == ele :
#             return midpoint
#         elif ele < mid_value :
#             end_index = midpoint - 1
#         else :
#             begin_index = midpoint + 1 
#     return None
# arr = [12,34,2,3,21,4,7]
# srt = sorted(arr)
# print(bianry_search(srt,34))

''' linear search '''

# def linear_search (arr,ele) :

#     for i in range(len(arr)) :
#         if arr[i] == ele :
#             return i


# arr = [12,34,2,3,21,4,7]
# srt = sorted(arr)
# print(linear_search(srt,34))



def mergesort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    else:
        mid = n // 2
        left, right = arr[:mid], arr[mid:]

        mergesort(left);mergesort(right)

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


myl = [7,0]
mergesort(myl)
print(myl)

