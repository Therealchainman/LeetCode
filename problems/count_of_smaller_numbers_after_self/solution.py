class Solution:
    def countSmaller(self, A):
        def merge(L, R):
            merged = []
            while L or R:
                if not R or L and L[-1][1] > R[-1][1]:
                    B[L[-1][0]] += len(R)
                    merged.append(L.pop())
                else:
                    merged.append(R.pop())
            merged.reverse()
            return merged
            
        def mergeSort(A):
            if len(A) <= 1:
                return A
            mid = len(A) >> 1
            L = mergeSort(A[:mid])
            R = mergeSort(A[mid:])
            return merge(L, R)
        
        E = list(enumerate(A))
        B = [0]*len(A)
        mergeSort(E)
        return B
    
    
"""
approach1:  Brute force O(n^2)
Iterate through i
iterate through elements after i comparing.
    def countSmaller(self, A):
        B = [0]*len(A)
        for i, vi in enumerate(A):
            for j in range(len(A))[i + 1:]:
                if A[j] < vi:
                    B[i] += 1
        return B

approach2:  Merge Sort O(nlogn)

"""
