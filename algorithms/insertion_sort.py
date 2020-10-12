"""
SORTING ALGORITHMS : INSERTION, SORTING DONE IN PLACE
    TIME COMPLEXITY : O(n^2) --> (n^2 because nested loops) --> AVG CASES

"""

arr = [53,41,4,5,1,25,20,-1] # unsorted array

def insertionsort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

print(insertionsort(arr))
