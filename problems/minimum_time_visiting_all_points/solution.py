import math
class Solution:
    def minTimeToVisitAllPoints(self, points):
        n=len(points)
        ans=0
        for i in range(1,n):
            x0,y0,x1,y1=points[i-1][0],points[i-1][1],points[i][0],points[i][1]
            ans+=max(abs(x0-x1),abs(y0-y1))
        return ans
        