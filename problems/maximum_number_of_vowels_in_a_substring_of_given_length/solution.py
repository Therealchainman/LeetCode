from collections import Counter
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = set("aeiou")
        ans = 0
        counter = 0
        for i in range(len(s) - k + 1):
            if i == 0:
                st = s[i:k+i]
                count = Counter(st)
                for v in vow:
                    if count[v]:
                        counter += count[v]
            if i > 0:
                if s[i - 1] in vow:
                    counter -= 1
                if s[k + i - 1] in vow:
                    counter += 1
            ans = max(counter, ans)
        return ans