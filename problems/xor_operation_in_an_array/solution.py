from itertools import accumulate
import operator
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2*i)
        return list(accumulate(arr, operator.xor))[-1]