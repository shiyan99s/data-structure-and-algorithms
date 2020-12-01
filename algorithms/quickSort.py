def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr.pop()
    items_greater , items_lower = [], []
    
    for item in arr:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


arr = [11173, 3241, 45241, 1431, 57, 234, 1, -1]
print(quickSort(arr))