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

