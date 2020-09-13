class Solution:
    def merge(self, A):
        events=[]
        for s,e in A:
            events.append((s,1))
            events.append((e,-1))
        count=0
        B=[]
        events.sort(key=lambda x: [x[0],-x[1]])
        for event, inc in events:
            count+=inc
            if count==1 and inc==1:
                start=event
            if count==0 and inc==-1:
                B.append([start,event])
                start=None
        return B
        