class Solution:
    def maxNonOverlapping(self, A,t):
        P=[0]
        for a in A:
            P.append(P[-1]+a)
        seen=set()
        ans=0
        for psum in P:
            if psum-t in seen:
                seen={psum}
                ans+=1
            else:
                seen.add(psum)
        return ans
                
        