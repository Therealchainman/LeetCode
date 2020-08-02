class Solution:
    def getWinner(self, A, k):
        count = 0
        prevW = curW = 0
        p1, p2 = 0, 1
        n = len(A)
        largest = max(A)
        while count < k:
            if A[p1] == largest:
                return largest
            if A[p1] > A[p2]:
                curW = A[p1]
                if prevW == curW == 0:
                    prevW = curW
                p2 += 1 
                p2 %= n
                if p2 == p1:
                    p2 += 1
                    p2 %= n
            else:
                curW = A[p2]
                if prevW == curW == 0:
                    prevW = curW
                p1 = p2
                p2 += 1 
                p2 %= n
            if prevW == curW:
                count += 1
            else:
                count = 1
            prevW = curW
        return curW