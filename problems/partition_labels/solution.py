class Solution:
    def partitionLabels(self, S):
        ret=[]
        last={c:i for i,c in enumerate(S)}
        start=end=0
        for i,s in enumerate(S):
            end=max(end,last[s])
            if i==end:
                ret.append(end-start+1)
                start=i+1
        return ret