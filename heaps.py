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
def main():
    arr = [50, 40, 50, 10, 15, 40]
    build_max_heap(arr)
    print(arr)
if __name__=='__main__':
     main()
x = 'X'
p = "X"
def printX():
    w = []
    x = [2, 4, 6]
    for i in x:
        w.append(i * 2)
        return w
print(printX())




#INTERVIEW QUESTIONS ON HEAPS

#QUESTION 1. Microsoft

#Initialize one empty array to help sort and another to store the sorted result.
def sorted_array(arr, k):
    min_heap = []
    results = []
#Fill the min-heap with the first k+1 elements    
    for i in range(min(len(arr), k + 1)):
        heapq.heappush(min_heap, arr[i])
    for i in range(k + 1, len(arr)):
#Add the next element to the heap, pop the smallest element and append it to the empty results list      
        heapq.heappush(min_heap, arr[i])
        results.append(heapq.heappop(min_heap))
#Add the rest of the elements to the result list    
    while min_heap:
        results.append(heapq.heappop(min_heap))
    return results

#example
arr = [7, 5, -2, -6, 4, 5]
k = 2
print(arr, k)



#QUESTION 2. Amazon
class ListNode:
   def __init__(self, value=0, next=None):
       self.value = value
       self.next = next


   def __lt__(self, other):
       return self.value < other.value


def merge_k_sorted_lists(lists):
   min_heap = []
  
   for l in lists:
       if l:
           heapq.heappush(min_heap, l)
  
   # Create a dummy node to help with result construction
   dummy = ListNode()
   current = dummy
  
   while min_heap:
       # Extract the smallest element
       node = heapq.heappop(min_heap)
       current.next = node
       current = current.next
       # If there are more elements in the same list, add the next element to the heap
       if node.next:
           heapq.heappush(min_heap, node.next)
  
   return dummy.next


# Helper function to print the linked list
def print_linked_list(node):
   while node:
       print(node.value, end=" -> ")
       node = node.next
   print("None")


# Example usage
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))


lists = [list1, list2, list3]
merged_list = merge_k_sorted_lists(lists)
print_linked_list(merged_list)




#QUESTION 3. Google
#create a function and initialize an empty array to keep track of the largest elements
def kth_largest(nums, k):
    min_heap = []
#loop through each number in the list
    for num in nums:
        heapq.heappush(min_heap, num)
#if the size of the min heap is greater than k, remove the smallest element        
        if len(min_heap) > k:
            heapq.heappop(min_heap)  
    return min_heap[0]


# Example usage
nums = [4, 2, 8, 5, 10, 4]
k = 3
third_largest = kth_largest(nums, k)
print(f"{k} is the third largest element.")



#QUESTION 4. Facebook
#Create a function then initialize an empty array to keep track of the k largest elements
def find_largest(nums, k):
   min_heap = []
#loop through the array then add the current number to the heap, if the size of the heap
#is greater than k, then pop the smallest element
   for num in nums:
       heapq.heappush(min_heap, num)
       if len(min_heap) > k:
           heapq.heappop(min_heap)
  
#     return min_heap[0]


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 3
third_largest = find_largest(nums, k)
print(f"The {k}rd largest element is {third_largest}")






#NO6. AMAZON
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add the new element at the end of the heap
        self.heap.append(value)
        # Restore the max-heap property
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursively heapify the parent
            self._heapify_up(parent_index)

    def __str__(self):
        return str(self.heap)

#example
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
print( heap)












def find_kth_largest(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
#     return min_heap[0]

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 3
third_largest = find_kth_largest(nums, k)
print(f"The {k}rd largest element is {third_largest}")