class Solution:
    def findKthPositive(self, A, k):
        p = 1
        j = 0
        for i,v in enumerate(A):
            if v == p :
                p=v+1
                continue
            j += v - p
            p=v+1
            if j >= k:
                diff = j-k
                return v-1-diff
        return A[-1] + k - j
        