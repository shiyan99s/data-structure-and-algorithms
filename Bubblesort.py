def bubblesort(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            for i in range(len(arr)-1-i):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            
    return(arr)

print(bubblesort([2363,23471,6,2,6,1,-1]))
