class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: [x[0],-x[1]])
        maxRight=0
        n=len(intervals)
        for s,e in intervals:
            if not maxRight:
                maxRight=e
                continue
            if e<=maxRight:
                n-=1
            maxRight=max(maxRight,e)
        return n
        
        
"""
approach:  line sweep algorithm

"""