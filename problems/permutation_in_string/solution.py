class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        contains = False
        if n1 == n2:
            if len(Counter(s1) - Counter(s2)) == 0:
                contains = True
            if n1 == n2 == 0:
                contains = False
        else:
            s = Counter(s1)
            window = Counter()
            for i in range(n2 - n1 + 1):
                if i == 0:
                    window = Counter(s2[:n1])
                else:
                    window[s2[i - 1]] -= 1
                    window[s2[i + n1 - 1]] += 1
                if (len(window - s) == 0):
                    return True
        return contains