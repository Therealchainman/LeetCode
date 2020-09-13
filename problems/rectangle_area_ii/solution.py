class Solution:
    def rectangleArea(self, R):
        mod=10**9+7
        events=[]
        for x1,y1,x2,y2 in R:
            events.append((y1,1,x1,x2))
            events.append((y2,-1,x1,x2))
        events.sort()
        def width():
            ret=0
            maxLeft=0
            for x1,x2 in active:
                maxLeft=max(maxLeft,x1)
                ret+=max(0,x2-maxLeft)
                maxLeft=max(maxLeft,x2)
            return ret
        ans=0
        active=[]
        cur_y=events[0][0]
        for y,inc,x1,x2 in events:
            ans+=(y-cur_y)*width()
            # I could also try insort method from python. 
            if inc==1:
                active.append((x1,x2))
                active.sort()
            else:
                active.remove((x1,x2))
            
            cur_y=y
        return ans%mod