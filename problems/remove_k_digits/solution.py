class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        queue = []
        for d in num:
            while queue and k and queue[-1] > d:
                queue.pop()
                k -= 1
            queue.append(d)
        res = ''.join(queue[:-k or None]).lstrip("0") or "0"
        return res