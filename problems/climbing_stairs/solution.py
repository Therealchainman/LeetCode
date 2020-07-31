class Solution:
    def climbStairs(self, n):
        pre = prev = 1
        for _ in range(n):
            pre, prev = prev, pre + prev
        return pre
            
        
        
"""
approach1:  Recursion  worst case there could be 2^45 operations
TLE O(2^n)

approach2:  JKIng DP, I'm saving sub problems values
Wait this is dynamic programming isn't
it it should be O(n) time complexity.  

approach3:  Could just use a for loop right






Fibonacci sequence, 1,1,2,3,5,8,13
1
1
1 way
2
1+1
2
2 ways

3
3 ways


4
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
5 ways

5
1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
1+2+2
2+1+2
2+2+1
8 ways

6
1+1+1+1+1+1
1+1+1+2+1
1+1+2+1+1
1+2+1+1+1
2+1+1+1+1
1+2+2+1
2+1+2+1
2+2+1+1
1+1+1+1+2
1+1+2+2
2+1+1+2
1+2+1+2
2+2+2
13 ways





"""