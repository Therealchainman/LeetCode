from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, B):
        if not B:
            return B
        events=[]
        # Add all the events to the events array including if it is left or right side of building.
        for li,ri,hi in B:
            events.append((li,-hi))
            events.append((ri,hi))
        # Sort the vents so that left sides come first and then sort based on right sides, and lastly sort
        # according to the heights. 
        events.sort(key=lambda x: [x[0],x[1]])
        active=SortedList(key=lambda x: -x)
        A=[]
        cur=prev=0
        for event,hi in events:
            if hi<0:
                active.add(-hi)
            else:
                active.remove(hi)
            cur=active[0] if len(active)>0 else 0
            if cur!=prev:
                A.append([event,cur])
                prev=cur
        return A
                
                    
                   
        