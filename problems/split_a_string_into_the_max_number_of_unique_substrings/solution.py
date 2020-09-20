class Solution:
    def maxUniqueSplit(self, s):
        seen=set()
        def dfs(s,seen):
            ans=0
            if s:
                for i in range(1,len(s)+1):
                    cand=s[:i]
                    if cand not in seen:
                        seen.add(cand)
                        ans=max(ans,1+dfs(s[i:],seen))
                        seen.discard(cand)
            return ans
        return dfs(s,seen)
        