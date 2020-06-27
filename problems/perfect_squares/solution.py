class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0 for _ in range(n + 1)]
        def minS(m):
            if memo[m]:
                return memo[m]
            i = 1
            best = m
            while i*i <= m:
                best = min(best, minS(m - i*i) + 1)
                i += 1
            memo[m] = best
            return memo[m]
            
        return minS(n)
            
        
"""
Start time: 12:44AM
approach1: O(nsqrt(n))
Hmm I juts don't know lol 
Let's do an example
say we have n = 13
memo = [0,1,2,3,1,2,3,4,2,1,2,3,4,2]
so 
it will take 
best = (13, minS(12) + 1)
best = (12, minS(11) + 1)
best = [(13,12,11,10,9,8,7,6,5)]
...
at the end it will reach
m = 0

Okay so m = 10
so we take best = 10
then take 
minS(10-1) = minS(9) = 1
so it is 
best = min(10, 2)

We pop 1 from the stack and compute the other side and we get 1
then we get to m = 4
At this point best = 4
i=1
and we already called on the previous values so we 
have best of 
best = min(4, 4) = 4 so best =4 sofar
But then we increment i=2
and again it works
so we take 
best = min(4, minS(0) + 1)
so best = 1
Ha that makes sense because you can just use a 4 to compute 4 using the perfect square of 4 will allow you to use the least
number of perfect squares to sum to 4. 

Okay we continue
to m = 5
now we have 
best = min(5, 5) = 5
but then increment i 
and we get best = min(5, minS(1) + 1)
so 2
then 6
and we get best = 6
at 7 what happens

then we hit 8
and this time we get best = 8
but then we incrmement i and we get 
best=(8, minS(4))
then increment i and we get 
min(5, minS(2) + 1)

But isn't minS(0) = 0
and so the while loop doesn't run and it returns
0 for memo[0]
Then we pull from this for our previous stack.  By popping from end
So we popp off the best(1, 1)
and we try to increment i but it fails.  
Then we try m=2
and best(1,2)

Then we try m =3 

Then we try m = 4 by popping fro mthe recursion stack. 
and this time best(3,4), but wait we increment i by one and this time it is still less than 4
So it adds to recursion stack with so we get another call
This time m = 0 again so oh we just return 0 
so it is best of (3, 1)


since m = 0 we get the 0 returned again don't we 
yeah it actually is already in memo so it returns 0
okay so then we go back to the stack with this zero
and what is th min(4, 1)
and 

"""