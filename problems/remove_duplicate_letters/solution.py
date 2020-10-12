class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        last_idx={ch:i for i,ch in enumerate(s)}
        res=[]
        vis=set()
        for i,ch in enumerate(s):
            if ch not in vis:
                while res and ch<res[-1] and i<last_idx[res[-1]]:
                    vis.remove(res.pop())
                res.append(ch)
                vis.add(ch)
        return "".join(res)