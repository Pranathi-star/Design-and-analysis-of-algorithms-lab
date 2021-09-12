import random
import time

class Solution:
    def partition(self, arr, l, r):
        pivot_idx = l
        pivot = arr[pivot_idx]
        while l < r:
            while l < len(arr) and arr[l] <= pivot:
                l += 1
            while arr[r] > pivot:
                r -= 1
            
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
        
        arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]
        return r
        
    def quick_sort(self, arr, l, r):
        if l < r:
            pivot_idx = self.partition(arr, l, r)
            self.quick_sort(arr, l, pivot_idx - 1)
            self.quick_sort(arr, pivot_idx + 1, r)

    def generate_random_arrays(self, size):
        array = []
        for i in range(size):
            array.append(random.randint(0, 500))
        return array

size1 = int(input("Enter size of array 1: ").strip())
arr = Solution()
arr1 = arr.generate_random_arrays(size1)

start_time = time.time()
arr.quick_sort(arr1, 0, size1 - 1)
end_time = time.time()
print("Time taken for quick sort: ", end_time - start_time)

size2 = int(input("Enter size of array 2: ").strip())
arr = Solution()
arr2 = arr.generate_random_arrays(size2)

start_time = time.time()
arr.quick_sort(arr2, 0, size2 - 1)
end_time = time.time()
print("Time taken for quick sort: ", end_time - start_time)