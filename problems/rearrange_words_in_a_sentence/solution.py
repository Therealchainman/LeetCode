from collections import defaultdict
class Solution:
    def arrangeWords(self, text: str) -> str:
        h = defaultdict(list)
        n = len(text)
        words = text.split()
        for w in words:
            h[len(w)] += [w]
        ret = ""
        for i in range(n):
            if h[i]:
                for word in h[i]:
                    ret += word + " "
        return ret.strip().lower().capitalize()
