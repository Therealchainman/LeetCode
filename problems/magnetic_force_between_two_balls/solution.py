class Solution:
    def maxDistance(self, A,m):
        A.sort()
        def possible(force):
            balls=1
            prev=A[0]
            for i,a in enumerate(A,1):
                if force<=a-prev:
                    balls+=1
                    prev=a
            return balls>=m
            
            
        def binary_search():
            lo,hi=0,A[-1]-A[0]
            while lo < hi:
                mid=lo+hi+1>>1
                if possible(mid):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        return binary_search()
        
"""
Type of problem where we have a function that takes in the force,
as force increases the number of balls decreases, thus it is a specific function that is monotonically decreasing
So for instance one thing that you can do is the following.  
Let's take a look at these below okay.  
Alright so how do I solve this haha, Let's take a closer look at the problem.  So I think it is basically just binary search again in a simple form where basically it is 
TTTTTFFFFF, that is as soon as we have less balls it is False right because that is not enough balls,  
So we want to return the last occurrence of T.  This requires a specific algorithm, 
So we understand what we are trying to achieve we are trying to find the last T in the sequence.  right because anytime the number of balls is less than required it is T, when you want to do this you need to use a specific algorithm, that has some idea,  Basically you need 

4-1=3 so the force=3
we have a ball at 1, then do we place a ball at 3, ummm, kind of yes,  

"""
        