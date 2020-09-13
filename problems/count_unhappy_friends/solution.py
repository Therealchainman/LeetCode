class Solution:
    def unhappyFriends(self, n,pref,pairs):
        ans=0
        graph=[0 for _ in range(n)]
        for x,y in pairs:
            graph[x]=y
            graph[y]=x
        def dfs(x,y):
            for u in pref[x]:
                if u==y:
                    break
                v=graph[u]
                for xx in pref[u]:
                    if xx==v:
                        break
                    if xx==x:
                        return True
            return False
        for x,y in pairs:
            if dfs(x,y):
                ans+=1
            if dfs(y,x):
                ans+=1
        return ans
        
        