''' linear search ''' 

def linear_search (arr,ele) :

    for i in range(len(arr)) :
        if arr[i] == ele :
            return i


arr = [12,34,2,3,21,4,7]
srt = sorted(arr)
print(linear_search(srt,34))


'''Binary Search'''

def bianry_search(arr,ele) :
    print(arr)
    begin_index = 0
    end_index = len(arr) - 1
    while begin_index <= end_index :
        midpoint = begin_index + (end_index - begin_index ) // 2
        mid_value = arr[midpoint]
        if mid_value == ele :
            return midpoint
        elif ele < mid_value :
            end_index = midpoint - 1
        else :
            begin_index = midpoint + 1 
    return None
    
arr = [12,34,2,3,21,4,7]
srt = sorted(arr)
print(bianry_search(srt,34))