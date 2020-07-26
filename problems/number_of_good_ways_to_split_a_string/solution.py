from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        ans = 0
        for i in range(len(s)-1):
            c = s[i]
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                ans += 1
        return ans
        
        # ls, rs = Counter(), Counter(s)
        # ld, rd = 0, len(Counter(s))
        # good = 0
        # for i in range(len(s) - 1):
        #     c = s[i]
        #     rs[c] -= 1
        #     if rs[c] == 0:
        #         rd -= 1
        #     if ls[c] == 0:
        #         ld += 1
        #     ls[c] += 1
        #     if rd == ld:
        #         good += 1
        # return good
            
        