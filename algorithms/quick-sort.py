"""
SORTING ALGORITHM : QUICK SORT
    TIME COMPLEXITY : O(nlogn)
"""

# implementation

def quicksort(arr):
    if len(arr) <= 1:  # base line for recursion
        return arr
    else:
        pivot = arr.pop()  # pivot, in this place last item in array

        item_lower = []   # list having elements lower than pivot
        item_greater = []  # list having elements greater than pivot

        for item in arr:   # adding elemnts into respective lists i.e lower/greater
            if item < pivot:
                item_lower.append(item)
            else:
                item_greater.append(item)

        return quicksort(item_lower) + [pivot] + quicksort(item_greater)   # returns [1..[pivot]....n]

arr = [5,4,3,2,1] # unsorted array

print(quicksort(arr))
