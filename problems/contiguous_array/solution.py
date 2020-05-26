class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        longest = sums = 0
        for i in range(len(nums)):
            length_subarray = 0
            if nums[i] == 1:
                sums += 1
            else:
                sums -= 1
            if sums == 0:
                length_subarray = i + 1
            elif sums not in dic:
                dic[sums] = i
            else:
                length_subarray = i - dic[sums]
            longest = max(length_subarray, longest)
        return longest
    
"""
Start time: 1:44 AM
Dynamic programming, break down into subproblems, 
[0]
"""




