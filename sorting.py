''' bubble sort '''
def bubble_sort(arr) :
    for i in range(len(arr)) :
        for j in range(len(arr)-i-1) :
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([23,1,6,312,3,2]))



''' selection sort '''

def selection_sort(arr) :
    for i in range(len(arr)) :
        min = i
        for j in range(i+1,len(arr)) :
            if arr[min] > arr[j] :
                min = j
        arr[i],arr[min] = arr[min],arr[i]

    return arr
print(selection_sort([23,123,1,3,21,2]))



'''Merge Sort'''

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
p = mergesort(myl)
print(p)


'''Insertion Sort'''

def InsertionSort(list_input):
    n = len(list_input)
    for i in range(1,n):
        key = list_input[i]

        j = i-1
        while j>=0 and key < list_input[j]:
            list_input[j+1] = list_input[j]
            j = j-1
        list_input[j+1] = key
        print(list_input)

InsertionSort([98,87,76,76,65,54])



'''Quick Sort'''
def quick_sort(arr) :
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
    return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)

print(quick_sort([12,34,1,2,63,98,43]))



'''Shell Sort'''

def shellsort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

a = [1,4,2,5,6,3,9,7]
shellsort(a)
print(a)