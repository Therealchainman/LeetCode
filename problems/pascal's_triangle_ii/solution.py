class Solution:
    def getRow(self, r):
        A = [1]
        for k in range(r):
            B=[1]
            for j in range(k):
                B.append(A[j] + A[j+1])
            B.append(1)
            A=B
        return A