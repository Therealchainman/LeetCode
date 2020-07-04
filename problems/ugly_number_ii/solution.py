class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        pointers = [0, 0, 0]
        numbers = [1]
        for _ in range(1, n):
            candidates = [factors[i] * numbers[pointers[i]] for i in range(len(factors))]
            newCandidate = min(candidates)
            numbers.append(newCandidate)
            pointers = [pointers[i] + (newCandidate == candidates[i]) for i in range(len(factors))]
        return numbers[-1]
"""
Start time: 3:50AM
approach1:  Min-Heap technique (Priority Queue)

approach2: dynamic programming

approach3:  math

The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.

Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""