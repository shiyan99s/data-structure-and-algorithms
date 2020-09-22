def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = mergesort(left)
        right = mergesort(right)

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

print(mergesort([5,1234,616,-1]))
