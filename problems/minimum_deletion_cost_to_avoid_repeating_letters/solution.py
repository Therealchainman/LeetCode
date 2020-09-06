import math
class SegTree:
    def __init__(self,arr):
        self.m=2**math.ceil(math.log2(len(arr)))
        inf=float('inf')
        self.arr=arr
        self.tree_sum=[0]*(2*self.m)
        self.tree_max=[-inf]*(2*self.m)
        self.n=len(arr)
        self.build_sum()
        self.build_max()
        
    def build_sum(self):
        for i in range(self.n):
            self.tree_sum[self.m+i]=self.arr[i]
        for i in range(self.m-1,0,-1):
            self.tree_sum[i]=self.tree_sum[i<<1]+self.tree_sum[i<<1|1]
        
    def build_max(self):
        for i in range(self.n):
            self.tree_max[self.m+i]=self.arr[i]
        for i in range(self.m-1,0,-1):
            self.tree_max[i]=max(self.tree_max[i<<1],self.tree_max[i<<1|1])
            
    def query_sum(self,l,r):
        l+=self.m
        r+=self.m
        ans=0
        while l<r:
            if l&1:
                ans+=self.tree_sum[l]
                l+=1
            if r&1:
                r-=1
                ans+=self.tree_sum[r]
            l>>=1
            r>>=1
        return ans
    
    def query_max(self,l,r):
        l+=self.m
        r+=self.m
        inf=float('inf')
        ans=-inf
        while l<r:
            if l&1:
                ans=max(ans,self.tree_max[l])
                l+=1
            if r&1:
                r-=1
                ans=max(ans,self.tree_max[r])
            l>>=1
            r>>=1
        return ans
    
class Solution:
    def minCost(self, s,cost):
        left=0
        ans=0
        st=SegTree(cost)
        for i,ch in enumerate(s):
            if ch!=s[left]:
                if i-1>left:
                    su=st.query_sum(left,i)
                    ma=st.query_max(left,i)
                    ans+=(su-ma)
                left=i
        right=len(s)
        if right>left:
            su=st.query_sum(left,right)
            ma=st.query_max(left,right)
            ans+=(su-ma)
        return ans
        