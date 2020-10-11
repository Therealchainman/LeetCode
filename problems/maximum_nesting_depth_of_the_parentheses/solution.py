class Solution:
    def maxDepth(self, s: str) -> int:
        bal=0
        ans=0
        for ch in s:
            if ch=="(":
                bal+=1
            elif ch==")":
                ans=max(ans,bal)
                bal-=1
            if bal<0:
                bal=0
        return ans