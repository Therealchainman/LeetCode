from random import randint
from random import shuffle
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        shuffle(nums)
        def quickSelect(arr, k, left, right):
            if left == right:
                return arr[left]
            pivot = partition(arr, left, right)
            if k - 1 == pivot:
                return arr[pivot]
            elif k - 1 < pivot:
                return quickSelect(arr, k, left, pivot - 1)
            else:
                return quickSelect(arr, k, pivot + 1, right)
        
        def partition(arr, left, right):
            i = left
            for j in range(left, right):
                if arr[j] > arr[right]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            if arr[i] < arr[right]:
                arr[i], arr[right] = arr[right], arr[i]
            return i
        
        return quickSelect(nums, k, 0, len(nums) - 1)
        
"""
This solution is using quick select algorithm
"""