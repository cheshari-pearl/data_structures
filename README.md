#QUESTION 1: Given an array where each element is at most K positions away from its sorted position, sort the array.
Heaps are useful here because they can efficiently manage and sort elements within a sliding window of size K.
A min-heap is used to help efficiently sort the elements.

#QUESTION 2: Given a list of integers nums and an integer k, write a function to return the k most frequent elements from the list.
This function counts the frequency of each element in the input list using the counter.
It then uses heapq.nlargest to find the k elements with the highest frequencies. This involves
creating a max-heap based on the frequencies of the elements. It will then return a list of these k most frequent elements.


#QUESTION 3: Given an array of integers, find the 3rd largest element in the array.
Use a min-heap to keep track of the top K largest elements seen so far.
Iterate through each element in the array.
Add each element to the min-heap.
If the heap exceeds size K, remove the smallest element from the heap. This ensures that the heap always contains the K largest elements encountered.
After processing all elements, the root of the min-heap will be the Kth largest element because the heap maintains the smallest of the largest K elements.



#QUESTION 4: Given an array of integers, write a function to find the k-th largest element in the array
This method uses a min-heap of size k to keep track of the k largest elements encountered. By the end of the iteration, the root of the min-heap (which is
the smallest of the k largest elements) is the k-th largest element in the array.


#QUESTION 5: How do you insert an element into a heap?
The Counter from the collections module is used to compute the frequency of each element in the list.
The code utilizes heapq.nlargest to retrieve the k elements with the highest frequencies.
The key=lambda x: x[1] argument ensures that the function compares elements based on their frequency.
