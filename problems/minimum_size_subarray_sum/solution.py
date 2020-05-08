class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = sumsy = 0
        count = 0
        queue = []
        for right in range(len(nums)):
            sumsy += nums[right]
            while sumsy >= s:
                sumsy -= nums[left]
                if sumsy < s:
                    minLength = min(minLength, right - left + 1)
                    left += 1
                    break
                left += 1
                # print(f"left={left}, right = {right} and sum = {sumsy}")
                minLength = min(minLength, right - left + 1)

        if minLength == float('inf'):
            return 0
        return minLength
                
                
                
            
            
            
            
            
            
'''
started at 6:48PM
How to fix such an issue lol?  I am so suspectingly dead.  
'''
            