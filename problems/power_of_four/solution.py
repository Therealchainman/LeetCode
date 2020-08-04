class Solution:
    def isPowerOfFour(self, n):
        return  n.bit_length() % 2 != 0 and n & (n - 1) == 0
    
"""
1000
0101
if you subtract 1
 yo uget
 0111
 and 
 0100
 and then & it 
 it should give you 0 if it is a power of 2
 
10
100
1000
10000
power of 2 has a 1 at the 2nd digit
and power of 4 has a 1 at the 3rd digit
and this pattern carries on with 
2-1
4-3
8-7
16-15
32-31
64 - 63
 
"""
        