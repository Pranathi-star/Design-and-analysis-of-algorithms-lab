# Program to find maximum element in array

import random
import time 

class Solution:
    def find_max_bruteforce(self, array):
        array.sort()
        return array[-1]

    def find_max_optimised(self, array):
        max_val = float('-inf')
        for item in array:
            if item > max_val:
                max_val = item
        return max_val

    def generate_random_arrays(self, size):
        array = []
        for i in range(size):
            array.append(random.randint(0, 500))
        return array

size1 = int(input("Enter the size of the array: "))
arr = Solution()

arr1 = arr.generate_random_arrays(size1)
print()

start_time = time.time()
arr.find_max_bruteforce(arr1)
print("Time taken for brute force solution: ", time.time() - start_time)
print("Max value using bruteforce: ", arr.find_max_bruteforce(arr1))

start_time = time.time()
arr.find_max_optimised(arr1)
print("Time taken for effective solution: ", time.time() - start_time)
print("Max value using efficient algo: ", arr.find_max_optimised(arr1))

print()

size2 = int(input("Enter the size of the array: "))

arr2 = arr.generate_random_arrays(size2)

print()
start_time = time.time()
arr.find_max_bruteforce(arr2)
print("Time taken for brute force solution: ", time.time() - start_time)
print("Max value using bruteforce: ", arr.find_max_bruteforce(arr2))

start_time = time.time()
arr.find_max_optimised(arr2)
print("Time taken for effective solution: ", time.time() - start_time)
print("Max value using efficient algo: ", arr.find_max_optimised(arr2))


