class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        def prefixSum(arr):
            for i in range(1,len(arr)):
                arr[i] += arr[i - 1] % MOD
            return arr
        prefixArr = [0]
        for i in range(n):
            temp = prefixSum(nums[i:])
            prefixArr.extend(temp)
        prefixArr.sort()
        p = prefixSum(prefixArr)
        return (p[right] - p[left-1]) % MOD