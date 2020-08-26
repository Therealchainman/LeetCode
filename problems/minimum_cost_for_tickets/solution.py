from collections import deque
class Solution:
    def mincostTickets(self, D,c):
        k=3
        P=[1,7,30]
        Q=[deque() for _ in range(k)]
        cost=0
        for d in D:
            for i in range(k):
                while Q[i] and Q[i][0][0]+P[i]<=d:
                    Q[i].popleft()
                Q[i].append((d,cost+c[i]))
            cost = min(Q[i][0][1] for i in range(k))
        return cost
        
"""
start time: 1:26AM
approach1:  DP
My first solution didn't work so redoing this with a queue now, 
Suppose we have the following days, 1,2,3,4,5,6,7,8,9,10,30,31
So then we take 
we update queue for 1, 7, and 30 days
[1,2]   [1,7]  [1,15]
next day we get
[2,4]   [[1,7],[2,9]]  [[1,15],[2,17]]
think about what this is doing this is basically adding 7 days to day 2 or starting the travel there which means we 
are at a cost of 9 because that is our minimal cost so far, 
This will repeat until
[7,14] [[1,7],[2,9],[3,11],[4,13],[5,9],[6,11],[7,13]]
then we realize that we can pop day 7 because the 1+7>d, 8>7 so that means we are over 7 days
so then we look at miminum cost,
[4,8], so now it choose 7 as cheaper
and now we get to 

[1,2]   [1,7],  [1,15]
[2,4]   [[1,7],[2,9]]   [[1,15],[1,17]]
[3,6]   [[1,7],[2,9],[3,11]]  [[1,15],[2,17],[3,19]]
cost=9
day 9
[9,11]  [[2,9],[3,11],[4,13],[5,14],[6,14],[7,14],[8,14]]  [[1,15],[2,17],[3,19],[4,21],[5,22],[6,22],[7,22],[8,22]]
1+7=8
1-7, 7 
6+7=13



"""