class Solution:
    def modifyString(self, s):
        offset=ord("a")
        ans=""
        for i,ch in enumerate(s):
            if ch=="?":
                for j in range(26):
                    cont=False
                    cand=chr(j+offset)
                    for idx in [i-1,i+1]:
                        if 0<=idx<len(s):
                            if s[idx]==cand:
                                cont=True
                        if 0<=idx<len(ans):
                            if ans[idx]==cand:
                                cont=True
                    if not cont:
                        ans+=cand
                        break
            else:
                ans+=ch
        return ans