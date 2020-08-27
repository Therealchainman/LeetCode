class Solution:
    def findRadius(self, houses,heaters):
        heaters.sort()
        inf=float('inf')
        heaters=[-inf]+heaters+[inf]
        ans=0
        
        def possible(val,target):
            return heaters[val]>=target
        
        def binary_search(target):
            lo,hi=0,len(heaters)-1
            while lo<hi:
                mid=lo+hi>>1
                if not possible(mid,target):
                    lo=mid+1        
                else:
                    hi=mid
            return lo
            
        for h in houses: 
            i=binary_search(h)
            print(i)
            dist=min(h-heaters[i-1],heaters[i]-h)
            ans=max(dist,ans)
        return ans
            
"""
So this problem can be solved with a binary search algorithm, let's see if I can figure out how to implement what type this is.  
Is it TTTFFF or FFFTTTT
so first off the data is that we are given heaters
so I'm thinking of iterating through the houses, and seeing what radius is required for it to be heated by the heaters, 
So think about this once you pick a house,  you just need to use binary search on the heaters to find the closest, heater to the target position,  
Then take that and use it to solve problem and you are done. 
so this is how it will work, 
we will try heaters from the beginning and the end,  so say we have [1,4]
now we will take the target,  and find when the house is between the heaters values.  that is lets say we have house 2
we will have lo=1,hi=4, and so uh the answer is 
Actually is it just me or is this a weird binary search algorithm problem.  it seems to be asking something very bizarre.  
So it seems to be the case that if lo<hi, we want to return something another.  but what I do not know.  lol

I'm trying to think of a good way to go about this though actually.  Here is my result haha,  take this below. 
if 
it is hard because what is mid, it is 
1,2,3,4
lo=1
hi=4
mid=2
When is it true and when false
Ive got it I want to return the first value fro mheaters where let's say it is true that the house is further away
so suppose house is 2
So that means the first true will be at 1,  

[1,2,3,4,5,6]
say house is 3
so the first true will be at 3, let's say if it is equal it is also true cause that makes the most sense \

FFTTTT, so this is good because we want to return the first T,  now to return the first T, means we are going to need the lo+hi methodology, very basic because it is going to move the last pointer in front and so on. 

major issue here is that there will be a part where it is negativ einfinity in which case that just sucks lol.  But regardless let me try to think of a strategy.  Iwhat if it is house=0
so then it will be FFFFFF, and it is never true unless we put a negative infinity, TFFFFF, suppose it it is larger than everything then we have TTTTT so add positive infinity to get TTTTF.  good 

house=2
FTT

"""    