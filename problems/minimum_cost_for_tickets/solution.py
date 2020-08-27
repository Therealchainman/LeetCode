
import bisect
class Solution:
    def mincostTickets(self, days,costs):
        
        @lru_cache(None)
        def dp(i):
            if i>=len(days):
                return 0
            return min(costs[0]+dp(bisect.bisect_left(days,days[i]+1)),
                      costs[1]+dp(bisect.bisect_left(days,days[i]+7)),
                      costs[2]+dp(bisect.bisect_left(days,days[i]+30))
                      )
        return dp(0)
        
"""
What is this lol?  So I have in my notes that this is a binary search problem.  but let's think about this for a moment.  The questions is asking to output the lowest cost for buying tickets right,  so I need to say there is a 1-day pass, a 7-day pass and another 1 day pass righgt,  sure but how do I find that 

I guess you could iterate through days, maybe, 

let think of the three tickets that I can get and how they relate to binary search.  

So for starters I could get ticket 1
so lets do a binary search to find the index I would reach in the table I guess,  


[1,4,6,7,8,20]
so search for 1+1=2, 
returns TFFFFF, lets return the first occurrence of true right and that would be the case for the algo that we move lo
then we take 7 day ticket and do 
1+7=8, and we iterate through and we will have TTTTFF, so we will say it is true only if less than the current value in iteration. 
then we have a simple problem becaues it is being broken down
Then we have that indexvalue and we continue our search from that index value.  
Another is the 30 days, 
For each of these we want to return the minimum total cost,  so it is just plus the rest, so we take the current cost and add
and this continues until base case where, if i is at end of list we return 0 because we do not need to travel anymore you know what I mean lol, this is just horrendous, so the base case would be if we run out of days right, then return 0
and at the end we want to return the minimum, also we can use dp because we will see similar cases, but ultimately if say we are at i=4,  if we see i=4 again it is the same thing, that is this problem can be broken down into smaller pieces 

Let's analyze what is happening here real quick.  So we have 
[1,4,6,7,8,20]
ans we have TFFFFFF, oh that is why it returns T, fair,  ummm,  I could switch it to 
FTTTTT, in which case anything that is greater than the target is true.  then I want to return the first occurrence of true. 


FFFFFF
"""
        