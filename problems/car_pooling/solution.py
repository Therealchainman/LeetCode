class Solution:
    def carPooling(self, A,c):
        events=[]
        for num,start,end in A:
            events.append((start,num))
            events.append((end,-num))
        events.sort()
        cur_num=0
        for event,delta in events:
            cur_num+=delta
            if cur_num>c:
                return False
        return True
            
        