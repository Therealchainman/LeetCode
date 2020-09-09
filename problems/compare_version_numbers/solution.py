class Solution:
    def compareVersion(self, v1,v2):
        A,B=v1.split("."),v2.split(".")
        for i in range(3):
            A.append("0")
            B.append("0")
        n = len(A) if len(A)<len(B) else len(B)
        for i in range(n):
            a,b=int(A[i]),int(B[i])
            if a<b:
                return -1
            if b<a:
                return 1
        return 0
        