# Solution uses the fact that
# n-(d-1)*n/d=n/d
class Solution:
    def minDays(self, n):
        stk=[n]
        ans=0
        vis=set()
        while stk:
            nstk=[]
            for x in stk:
                if x in vis:
                    continue
                if x==0: 
                    return ans
                nstk.append(x-1)
                if x%2==0: 
                    nstk.append(x//2)
                if x%3==0: 
                    nstk.append(x//3)
                vis.add(x)
            ans+=1
            stk=nstk
        