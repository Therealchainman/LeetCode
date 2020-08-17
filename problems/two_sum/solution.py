from collections import defaultdict
class Solution:
    def twoSum(self, A,t):
        D={}
        n=len(A)
        for i,a in enumerate(A):
            if t-a in D:
                return [D[t-a],i]
            else:
                D[a]=i
        return []
        