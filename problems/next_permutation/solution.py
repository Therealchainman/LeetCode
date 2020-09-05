class Solution:
    def nextPermutation(self, A):
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            A[i],A[j]=A[j],A[i]
            
        def reverse(idx,length):
                k=1
                for i in range(idx,length):
                    if length-k<=i:
                        break
                    swap(i,length-k)
                    k+=1
                    
        def possible(idx,target):
            return A[idx]>target
            
        def binary_search(lo,hi,target):
            while lo < hi:
                mid = lo+hi+1>>1
                if possible(mid,target):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        
        n=len(A)
        idx=-1
        for i in range(1,n):
            if A[i]>A[i-1]:
                idx=i-1
        if idx==-1:
            reverse(0,n)
            return
        j=binary_search(idx+1,n-1,A[idx])
        swap(idx,j)
        reverse(idx+1,n)
            
"""
TTTFFF
FFFTTT
return first occurence of T.  So I can't use something lol.  Not sure what though haha.  


"""