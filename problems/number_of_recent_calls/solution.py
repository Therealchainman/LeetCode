import heapq
class RecentCounter:

    def __init__(self):
        self.rec=[]

    def ping(self, t):
        lower_bound=t-3000
        heapq.heappush(self.rec,t)
        while self.rec[0]<lower_bound:
            heapq.heappop(self.rec)
        return len(self.rec)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)