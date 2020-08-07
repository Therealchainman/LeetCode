class Solution:
    def findDuplicates(self, A):
        n=len(A)
        res=[]
        for a in A:
            if A[abs(a) - 1] < 0:
                res.append(abs(a))
            else:
                A[abs(a)-1]*=-1
        return res
            
        
"""
start time: 7:15pm
approach1: Breaks down if n>32

approach2:  






"""