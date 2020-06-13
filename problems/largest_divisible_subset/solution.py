class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        # sorting
        nums.sort()
        # filling our count array
        count = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i - 1, -1,-1):
                if nums[i] % nums[j] == 0:
                    count[i] = max(count[i], count[j] + 1)
        # finding the max index
        maxIndex = 0
        bestCount = 0
        for i in range(n):
            if count[i] > bestCount:
                maxIndex = i
            bestCount = max(bestCount, count[i])
        counter = count[maxIndex]
        res = []
        # Reconstructing the subset
        for i in range(maxIndex, -1, -1):
            if counter == 0:
                break
            if count[i] == counter and nums[maxIndex] % nums[i] == 0:
                counter -= 1
                res.append(nums[i])
        return res
        
"""
Start time: 3:17PM

"""