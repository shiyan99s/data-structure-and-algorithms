"""
BUBBLE SORT ALGORITHM :
"""

def Bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(Bubblesort([5,4,3,2,1]))
