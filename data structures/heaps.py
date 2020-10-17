import heapq

#random list
arr = [5, 7, 9, 1, 3, 2]

#converting arr(list) into heaps using heap.*heapify* function
heapq.heapify(arr)
"""
    arr = [5, 7, 9, 1, 3, 2]
        heapify -->
            5
           /  \
          7    9
         / \    \
        1   3    2
"""

#printing modified arr back into list type
print(arr)

#pushing element into heap(arr) using *heapq.heappush*
heapq.heappush(arr, 10)
print(arr)

popped = heapq.heappop(arr)

print(popped)

# heapq.heappushpop(arr, 2)
# heapq.heapreplace(arr, -1)
