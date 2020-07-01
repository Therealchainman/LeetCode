import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) >> 1
            nk = k*(k + 1) // 2
            if nk == n:
                return k
            elif nk < n:
                left = k + 1
            else:
                right = k - 1
        return right
        
        
"""
approach1: using completing the square, O(1), O(1)

approach2: binary search
We can get

k^2 + k
odd number * odd number = odd number
odd number + odd number = even number

even number * even number = even number
even number + even number = even number


n = 8

0,1,2,3,4,5,6,7,8
    ^ ^       
    ^


"""