"""
SEARCHING ALGORITHM : BINARY SEACH
    TIME COMPLEXITY : O(log(n))

"""

def BinarySearch(arr, left, right, find_val):
    if right >= left:
        mid = left + (right - 1) // 2    # stores index number

        if arr[mid] == find_val:
            return mid

        elif arr[mid] > find_val:
            return BinarySearch(arr, left, mid - 1, find_val)  # left recursion

        else:
            return BinarySearch(arr, mid + 1, right, find_val) # right recursion


arr = [1,2,3,4,5,6,7]

print(BinarySearch(arr, 0, len(arr)-1 , 5))  # len(arr) - 1 : so index stays in range
