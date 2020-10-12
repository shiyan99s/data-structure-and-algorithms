"""
MERGE SORT ALGORITHM : Recursive method
"""


def MergeSort(arr):
    if len(arr) > 1:
        mid_point = len(arr) // 2   # mid_point of arr
        left = arr[:mid_point]
        right = arr[mid_point:]

        left = MergeSort(left)
        right = MergeSort(right)

        arr = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)

        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)

    return arr

"""
Checking MergeSort
"""
arr = [11173, 3241, 45241, 1431, 57, 234, 1, -1]
print(MergeSort(arr))
