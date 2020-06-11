class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, twos = 0, len(nums) - 1
        i = 0
        while i <= twos:
            if nums[i] == 0:
                nums[zeros], nums[i] = nums[i], nums[zeros]
                zeros += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[twos], nums[i] = nums[i], nums[twos]
                twos -= 1
            
        
        
"""
Approach 1: O(n^2) Brute force
basically modified selection sort algorithm

Approach 2: one-pass algorithm, using constant space.  

"""