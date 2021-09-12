import random
import time

class Solution:
    def merge(self, arr, l, mid, r):
        n1 = mid - l + 1
        n2 = r - mid

        left_half, right_half = [0] * n1, [0] * n2

        for i in range(n1):
            left_half[i] = arr[l + i]
        
        for j in range(n2):
            right_half[j] = arr[mid + 1 + j]

        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1

            else:
                arr[k] = right_half[j]
                j += 1
            
            k += 1
        
        while i < n1:
            arr[k] = left_half[i]
            k += 1
            i += 1
        
        while j < n2:
            arr[k] = right_half[j]
            k += 1
            j += 1

    def merge_sort(self, arr, l, r):
        if l < r:
            mid = l + (r - l)//2
            self.merge_sort(arr, l, mid)
            self.merge_sort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

    def generate_random_arrays(self, size):
        array = []
        for i in range(size):
            array.append(random.randint(0, 500))
        return array

size1 = int(input("Enter size of array 1: ").strip())
arr = Solution()
arr1 = arr.generate_random_arrays(size1)

start_time = time.time()
arr.merge_sort(arr1, 0, size1 - 1)
end_time = time.time()
print("Time taken for merge sort: ", end_time - start_time)

size2 = int(input("Enter size of array 2: ").strip())
arr = Solution()
arr2 = arr.generate_random_arrays(size2)

start_time = time.time()
arr.merge_sort(arr2, 0, size2 - 1)
end_time = time.time()
print("Time taken for merge sort: ", end_time - start_time)
