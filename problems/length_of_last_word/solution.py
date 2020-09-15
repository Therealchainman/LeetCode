class Solution:
    def lengthOfLastWord(self, s):
        n=len(s)
        ans=0
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                ans+=1
            elif ans>0:
                return ans
        return ans
        