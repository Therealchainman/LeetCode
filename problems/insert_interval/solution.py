class Solution:
    def insert(self, I,NI):
        events=[]
        I.append(NI)
        for s,e in I:
            events.append((s,1))
            events.append((e,-1))
        events.sort(key=lambda x: [x[0],-x[1]])
        A=[]
        count=0
        for event, inc in events:
            count+=inc
            if count==1 and inc==1:
                start=event
            if count==0 and inc==-1:
                A.append([start,event])
                start=None

        
        return A
    
"""
approach: Sweep Line algorithm

"""
        