class Solution:
    def findRadius(self, houses, heaters):
        heaters=[-float('inf')]+heaters+[float('inf')]
        heaters.sort()
        houses.sort()
        ans=i=0
        for h in houses:
            while h>=heaters[i+1]:
                i+=1
            dist=min(h-heaters[i],heaters[i+1]-h)
            ans=max(dist,ans)
        return ans
"""
Let's do this with binary search with bisect module in python

[1,2,3,4,5]
[1,5]
r=2
[0,3],[3,7]
1 1 is less than the end point
so keep going, should I check that it is greater than the start point? 
1<endpoint
2<endpoint
3<endpoint
4 is not smaller than endpoint
increment ito next interval
and now 4 is smaller than its endpoint
in addition 4 is not smaller than the start, if it was we are doomed


"""
        