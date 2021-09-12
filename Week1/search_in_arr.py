# Program to search element in array

import random
import time 

class Solution:
    def search_bruteforce(self, array, target):
        for i in array:
            if i == target:
                return "Present in array"
        return "Not present in array"
        
    def binary_search_util(self, array, low, high, target):
        while low <= high:
            mid = (low + high) >> 1
            if array[mid] == target:
                return "Present in array"
            elif array[mid] > target:
                return self.binary_search_util(array, low, mid - 1, target)
            elif array[mid] < target:
                return self.binary_search_util(array, mid + 1, high, target)
        return "Not present in array"

    def search_optimised(self, array, target):
        return self.binary_search_util(array, 0, len(array) - 1, target)

    def generate_random_arrays(self, size):
        array = []
        for i in range(size):
            array.append(random.randint(0, 500))
        return array

size1 = int(input("Enter the size of the array: "))
arr = Solution()

arr1 = arr.generate_random_arrays(size1)
target = random.randint(0, 500)
print("Target is: ", target)


print()
start_time = time.time()
arr.search_bruteforce(arr1, target)
print("Time taken for brute force solution: ", time.time() - start_time)
print(arr.search_bruteforce(arr1, target))

arr1.sort()
start_time = time.time()
arr.search_optimised(arr1, target)
print("Time taken for effective solution: ", time.time() - start_time)
print(arr.search_optimised(arr1, target))

print()

size2 = int(input("Enter the size of the array: "))

arr2 = arr.generate_random_arrays(size2)

target = random.randint(0, 1000)
print("Target is: ", target)

print()
start_time = time.time()
arr.search_bruteforce(arr2, target)
print("Time taken for brute force solution: ", time.time() - start_time)
print(arr.search_bruteforce(arr2, target))

arr2.sort()
start_time = time.time()
arr.search_optimised(arr2, target)
print("Time taken for effective solution: ", time.time() - start_time)
print(arr.search_optimised(arr2, target))


