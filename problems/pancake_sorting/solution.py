class Solution:
    def pancakeSort(self, A):
        k=len(A)
        ans=[]
        
        while k>1:
            index=A[:k].index(k)+1
            ans.extend([index,k])
            A=A[:index][::-1]+A[index:]
            A=A[:k][::-1]+A[k:]
            k-=1
        return ans