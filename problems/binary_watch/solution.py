class Solution:
    def readBinaryWatch(self, n):
        
        def dfs(n,h,m,idx):
            if h>11 or m>59:
                return
            if not n:
                ans.append(str(h) + ":" + str(m).zfill(2))
                return
            for i in range(idx,10):
                if i < 4:
                    dfs(n-1,h | (1<<i),m,i+1)
                else:
                    k=i-4
                    dfs(n-1,h,m |(1<<k),i+1)
            
        ans=[]
        dfs(n,0,0,0)
        return ans
        