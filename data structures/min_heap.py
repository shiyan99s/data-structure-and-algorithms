import heapq

heap = []
heapq.heapify(heap)

#adding elements to heap using heapq.heappush()
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 400)

arr = []
for item in heap:
    arr.append(item)

#prints min heap in organised way
print(arr)
