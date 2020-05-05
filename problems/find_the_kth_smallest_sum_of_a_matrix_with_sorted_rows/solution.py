class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = mat[0]
        for row in mat[1:]:
            heap = sorted([i + j for i in row for j in heap])[:k]
        return heap[k - 1]
        