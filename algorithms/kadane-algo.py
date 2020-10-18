"""
    KADANE's ALGORITHM :  maximum contiguous subarray
"""
from sys import maxsize

def kadaneAlgo(arr):
    checked = - maxsize
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
