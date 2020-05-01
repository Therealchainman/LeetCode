class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best = sum(cardPoints[:k])
        s = best
        n = len(cardPoints)
        for i in range(1, k + 1):
            s -= cardPoints[k - i]
            s += cardPoints[n - i]
            best = max(s, best)
        return best