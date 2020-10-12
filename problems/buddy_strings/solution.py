class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n,m=len(A),len(B)
        if n!=m or set(A)!=set(B):
            return False
        if A==B:
            return n-len(set(A))>0
        indices=[]
        counter=0
        for i in range(n):
            if A[i]!=B[i]:
                counter+=1
                indices.append(i)
            if counter>2:
                return False
        return A[indices[0]]==B[indices[1]] and A[indices[1]]==B[indices[0]]