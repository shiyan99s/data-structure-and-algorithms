"""
SEARCHING ALGORITHM : LINEAR SEARCH
    TIME COMPLEXITY : O(n)
    Iterate over every element and check whether element to be search equal to it
"""
def LinearSearch(arr, find_val):
    for item_index in range(len(arr)):  # iterate over every element
        if arr[item_index] == find_val:  # checking condition
            return ("item is at {} index".format(item_index))  # returns index value (position)

    else:
        return ("item not in array")  # returns false, if not found



arr = [22,63,732,1,34,124]
print(LinearSearch(arr, 22))
