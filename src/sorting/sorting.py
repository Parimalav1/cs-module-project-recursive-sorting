# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # Your code here
    merged_arr = []
    a = 0
    b = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1

    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
# def merge_sort( arr ):
#     if len( arr ) > 1:
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces

# def merge_helper( a, b ):
#     merged_arr = []

    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    # return merged_arr


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        arr = merge(left, right)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # merged_arr = [0] * elements
    # Your code here
    a = start
    b = mid
    while a < b and b <= end:
        if arr[a] <= arr[b]:
            a += 1
        else:
            temp = arr[b]
            j = b
            while j > a:
                arr[j] = arr[j-1]
                j -= 1
            arr[a] = temp
            b += 1
            a += 1               
 

def merge_sort_in_place(arr, l, r):
    # Your code here
    # Your code here
    arr_len = r - l + 1
    if arr_len <= 1:
        pass
    else:
        mid = (l + r) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid + 1, r)

# helper function to partition the input array 
def partition(arr):
    # pick a pivot 
    pivot = arr[0]
    left = []
    right = []
    
    # partition the elements around the pivot 
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # we have elements partitioned in the left, pivot, and right arrays 
    return left, pivot, right 

def quicksort(arr):
    # base case if len array <= 1 
    if len(arr) <= 1:
        return arr

    # otherwise, we need to call our partition function to break the inpu
    # array into smaller chunks 
    left, pivot, right = partition(arr)
    
    # stick the pivot in a list 
    pivot = [pivot]

    # run quicksort on left and right chunks 
    # to break them down further into smaller pieces 
    qleft = quicksort(left)
    qright = quicksort(right)

    # concatenate all the pieces together 
    return qleft + pivot + qright
        

arr = [13, 17, 5, 18, 27, 22, 16, 3]
arr = quicksort(arr)
print(arr)
# def quicksort(array):
#     if len(array) < 2:
#         # Base case: arrays with 0 or 1 element are already "sorted"
#         return array
#     else:
#         # Recursive case
#         pivot = array[0]
#         # Sub-array of all the elements less than the pivot
#         less = [ i for i in array[1:] if i <= pivot]
#         # Sub-array of all the elements greater than the pivot
#         greater = [i for i in array[1:] if i > pivot]

#         return quicksort(less) + [pivot] + quicksort(greater)