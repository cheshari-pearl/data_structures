import heapq

nums = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
heapq.heapify(nums)

print( nums)

print( heapq.heappop(nums))
print( nums)

heapq.heappush(nums, 9)
heapq.heappush(nums, 0)
print( nums)

print( nums[0])

print( heapq.nsmallest(4, nums))
print( heapq.nlargest(2, nums))

print( heapq.heappushpop(nums, 30))
print( nums)

while nums:
    print( heapq.heappop(nums))

print( nums)


#max heaps
def max_heapify(arr, j):
    l = left(j)
    r = right(j)
    if l < len(arr) and arr[l] > arr[j]:
        largest = l
    else:
        largest = j
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != j:
        arr[j], arr[largest] = arr[largest], arr[j]
        max_heapify(arr, largest)
def left(j):
    return 2 * j + 1
def right(j):
    return 2 * j + 2
def build_max_heap(arr):
    n = int((len(arr)//2)-1)
    for j in range(n, -1, -1):
        max_heapify(arr, j)
def main(









