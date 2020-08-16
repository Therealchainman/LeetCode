class Solution:
    def eraseOverlapIntervals(self, A):
        A.sort(key=lambda x: (x[1],x[0]))
        
        ans=0
        latest=-float('inf')
        for s,e in A:
            if s < latest:
                ans+=1
            else:
                latest=max(latest,e)
        return ans

        