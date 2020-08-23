from collections import Counter
class Solution:
    def mostVisited(self, n,R):
        count=Counter()
        for i in range(1,len(R)):
            start=R[i-1]
            end=R[i]%(n+1)
            if end==0:
                end+=1
            while start!=end:
                count[start]+=1
                start=(start+1)%(n+1)
                if start==0:
                    start+=1
        count[start]+=1
        goal=max(count.values())
        res=[x for x,y in count.items() if y==goal]
        res.sort()
        return res
        