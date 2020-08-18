class Solution:
    def distributeCandies(self,c,n):
        prev=i=0
        res=[0]*n
        while c>0:
            prev+=1
            res[i%n]+=min(c,prev)
            c-=prev
            i+=1
        return res
        