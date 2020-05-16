class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curMax, totalMax, curMin, totalMin, total = 0, float('-inf'), 0, float('inf'), 0
        for elem in A:
            curMax = max(elem, curMax + elem)
            totalMax = max(curMax, totalMax)
            curMin = min(elem, curMin + elem)
            totalMin = min(curMin, totalMin)
            total += elem
        final = max(totalMax, total - totalMin)
        return final if final != 0 else max(A)
