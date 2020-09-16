# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # for i in range(0, len(arr)):
    #     midpoint = (start + end) // 2
    #     guess = arr[midpoint]
    #     if guess == int(target):
    #         return midpoint
    #     if guess > int(target): # LHS
    #         midpoint - 1
    #         print(midpoint - 1)
    #     else:  # RHS
    #         midpoint + 1
    # return -1
    # set the base case
    if end >= start:
        # start = 0
        # end = len(arr) - 1
        midpoint = (start + end) // 2
        guess = arr[midpoint]
        #  recursive implementation
        if guess == target:
            return midpoint
        elif guess > target:  # LHS
            return binary_search(arr, target, 0, midpoint - 1)
        else:  # RHS
            return binary_search(arr, target, midpoint + 1, end)
    else:
        return -1


test = [2, 4, 7, 8, 9, 10, 12, 34, 45]
binary_search(test, 9, 0, len(test) - 1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
#     pass
