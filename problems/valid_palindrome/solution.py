class Solution:
    def isPalindrome(self, S):
        S = S.lower()
        SS=""
        for c in S:
            if ord("a")<=ord(c)<=ord("z") or ord("0")<=ord(c)<=ord("9"):
                SS+=c
        l,r=0,len(SS)-1
        while l < r:
            if SS[l]!=SS[r]:
                return False
            l+=1
            r-=1
        return True
        