"""
SORTING ALGORITHM : SELECTION SORT
    TIME COMPLEXITY : O(n^2) --> (n^2 because are two nested loops)
    Auxiliary Space: O(1)
    The good thing about selection sort is it never makes more than O(n)
    swaps and can be useful when memory write is a costly operation.
"""

arr = [5,3,12,61,231,7,1,-1] # unsorted array

def selectionsort(arr):
    for i in range(len(arr)):
        # minimum index
        min_index = i
        # find minimum element in the remaining unsorted array
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selectionsort(arr))
