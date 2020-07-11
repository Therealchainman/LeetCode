class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        longest = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            longest = max(longest, dp[i])
        return longest
    
"""
approach1:  Brute force through with a dp table.  
The basic idea, is that 
[10,9,2,5,3,7,101,2]
                   ^
                ^
 
 possible increasing subsequences = [2,7]
 dp = [1,1,1,2,2,3,4,4]
 
 You already computed the longest increasing subsequence in the sub problem that deals with arr[3] = 5,  We know that we can have [2,5] as 
 the longest increasing subsequence.  Now we also know that 5 is less than 7 so we could add one more element to it to get 
 a length of 3
"""