import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cands=string.ascii_lowercase
        S=""
        for ch in s:
            if ch.lower() in cands or ch in string.digits:
                S+=ch.lower()
        n=len(S)
        return all(S[k]==S[n-1-k] for k in range(n>>1))

        
            