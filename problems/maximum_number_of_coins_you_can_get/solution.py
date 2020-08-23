class Solution:
    def maxCoins(self, P):
        P.sort()
        dq=deque(P)
        ans=0
        while dq:
            bob=dq.popleft()
            alice=dq.pop()
            me=dq.pop()
            ans+=me
        return ans
        