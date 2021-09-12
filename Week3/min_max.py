import random
import time

class Solution:
    def getMinMax_bruteforce(self, arr):
        arr_min = arr[0]
        arr_max = arr[0]
        for i in arr:
            if i < arr_min:
                arr_min = i
            if i > arr_max:
                arr_max = i
        return (arr_max, arr_min) 

    def getMinMax_optimized(self, low, high, arr):
        arr_max = arr[low]
        arr_min = arr[low]
        
        # If there is only one element
        if low == high:
            arr_max = arr[low]
            arr_min = arr[low]
            return (arr_max, arr_min)
            
        # If there is only two element
        elif high == low + 1:
            if arr[low] > arr[high]:
                arr_max = arr[low]
                arr_min = arr[high]
            else:
                arr_max = arr[high]
                arr_min = arr[low]
            return (arr_max, arr_min)
        else:
            
            # If there are more than 2 elements
            mid = int((low + high) / 2)
            arr_max1, arr_min1 = self.getMinMax_optimized(low, mid, arr)
            arr_max2, arr_min2 = self.getMinMax_optimized(mid + 1, high, arr)
    
        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

    def generate_random_arrays(self, size):
        array = []
        for i in range(size):
            array.append(random.randint(0, 500))
        return array

size1 = int(input("Enter size of array 1: ").strip())
arr = Solution()
arr1 = arr.generate_random_arrays(size1)

start_time = time.time()
res = arr.getMinMax_bruteforce(arr1)
end_time = time.time()
print("Time taken for bruteforce algo: ", end_time - start_time)
print("Min-Max pair: ", res)

start_time = time.time()
res = arr.getMinMax_optimized(0, size1 - 1, arr1)
end_time = time.time()
print("Time taken for optimized algo: ", end_time - start_time)
print("Min-Max pair: ", res)

