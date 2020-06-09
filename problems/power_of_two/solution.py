class Solution:
    def isPowerOfTwo(self, n: int) -> bool: 
        if n <= 0: 
            return False
        return n & -n == n
        
        
"""
Start time: 3:43PM
Approach1: Bit manipulation, O(1), O(1)
&: logical operator --> check if bit is on or not.  
16 -> 0001 0000
&
16 - 1 -> 0000 1111
0

1 -> 0000 0001
&
0 -> 0000 0000
0

7 -> 0000 0111
&
7 - 1 -> 0000 0110
0000 0110



"""