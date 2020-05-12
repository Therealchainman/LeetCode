class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            mid = 2 * ((l + r) >> 2)
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]
            
        
        
        
'''
8:40AM
'''