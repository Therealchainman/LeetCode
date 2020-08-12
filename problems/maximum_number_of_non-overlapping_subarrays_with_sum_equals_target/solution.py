class Solution:
    def maxNonOverlapping(self, A,t):
        P=[0]
        for a in A:
            P.append(P[-1]+a)
        s=set()
        ans=0
        for p in P:
            if p-t in s:
                s={p}
                ans+=1
            else:
                s.add(p)
        return ans
        