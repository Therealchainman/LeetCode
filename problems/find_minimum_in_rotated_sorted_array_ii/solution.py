class Solution:
    def findMin(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n - 1
        while l < r:
            m = (l + r) >> 1
            if nums[r] < nums[m]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m
                l += 1
            elif nums[l] < nums[m] or nums[l] < nums[r]:
                r = m - 1
            else:
                r -= 1
                l += 1
        return nums[l]
            
                

        
"""
Start time: 6:16AM
(m, r]
(l, m]

approach1:  binary search algorithm

[3,3,1,3]
 l m   r

[2,2,2,0,1]
       l  r 
       m
[10,1,10,10,10]
 r           l

[5,6,7,0,1,2,4]
     l r
     m    
[2,2,2,0,1]
       l  r

"""