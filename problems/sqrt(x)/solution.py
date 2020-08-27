class Solution:
    def mySqrt(self, x):
        
        def possible(y):
            return y<=x/y
        def binary_search():
            lo,hi=0,x
            while lo<hi:
                mid=lo+hi+1>>1
                if possible(mid):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        return binary_search()
        
        
"""
Alright, lets do this with a binary search,  
It will be simple, suppose we have  8
what is the square root of 8,  
we could set lo=1 and hi=8
then mid is 4, and does 4 work?  uhhh yeah how do I test lol.  
I was thinking I could actually compute square root but no
I could also square it and say hey the square is greater than 8 so it is False right, 


TTFFFFF, 
so return the last occurrence of T,  it will be the largest value that will not exceed 8, but works
the only issue really is what is my definition of possible doing lol?  
Does it seem reasonable to be squaring in this.  

Al right this is one solution with thinking in terms of trying to find a solution that contained binary search, can I use bits in here though as well,  
10
1000
so 10
100
10

"""
        