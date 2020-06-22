from itertools import accumulate
import operator
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = 0
        for i in range(n):
            x ^= (start + i*2)
        return x
    
    
"""
[1,2,3,4,5]
-> [1, 2+1=3, 3+3=6, 6+4=10, 1+2+3+4+5]
[]
accumulate(arr, operator.mul)
"""