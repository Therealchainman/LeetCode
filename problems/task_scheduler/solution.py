class Solution:
    def leastInterval(self, T,n):
        count=[0]*26
        offset=ord("A")
        for t in T:
            count[ord(t)-offset]+=1
        count.sort()
        max_val=count[25]-1
        idle_slots=max_val*n
        for i in range(24,-1,-1):
            idle_slots-=min(count[i],max_val)
        return idle_slots+len(T) if idle_slots>=0 else len(T)

            
                     
        
        
"""
A->B->idle->A->B->idle->A->B
t=1,2,3
heap=[(A,3),(B,4)]
"""
        