import operator
from itertools import accumulate
class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            del numbers[index]

        return permutation
        
        
"""
Start time: 2:30PM
approach1: time O(n^2 + k*n -> O(n),)


"""
        