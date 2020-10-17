"""
    KADANE's ALGORITHM :  maximum contiguous subarray
"""

def kadaneAlgo(arr):
    checked = 0
    checking = 0

    for i in range(len(arr)):
        checking += arr[i]
        if checked < checking:
            checked = checking
        if checking < 0:
            checking = 0

    return checked

arr = [-2, -3, 4, -1, -2, 1, 5, -3]  # arr to find max subrray sum

print(kadaneAlgo(arr))  # print 7
