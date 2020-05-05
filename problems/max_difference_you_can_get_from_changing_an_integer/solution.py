class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNums = float('-inf')
        minNums = float('inf')
        for i in "0123456789":
            for j in "0123456789":
                nextnum = num.replace(i,j)
                if nextnum[0] == "0" or int(nextnum) == 0:
                    continue  
                maxNums = max(maxNums, int(nextnum))
                minNums = min(minNums, int(nextnum))
        return maxNums - minNums