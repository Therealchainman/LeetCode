class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)
        for i, v in enumerate(s):
            idx = indices[i]
            res[idx] = v
        return "".join(res)