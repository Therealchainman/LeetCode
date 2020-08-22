class Solution:
    def maxDistance(self, P,m):
        P.sort()
        def numberBalls(force):
            prev=P[0]
            balls=1
            for i,p in enumerate(P):
                if p-prev>=force:
                    prev=p
                    balls+=1
            return balls
        lo, hi=1,P[-1]-P[0]
        while lo<hi:
            mid=(lo+hi+1)>>1
            # print(lo, hi,mid, numberBalls(mid))
            if numberBalls(mid)>=m:
                lo=mid
            else:
                hi=mid-1
        return lo
#     def maxDistance(self, position: List[int], m: int) -> int:
#         n = len(position)
#         position.sort()
        
#         def count(d):
#             ans, curr = 1, position[0]
#             for i in range(1, n):
#                 if position[i] - curr >= d:
#                     ans += 1
#                     curr = position[i]
#             return ans
        
#         l, r = 1, position[-1] - position[0]
#         while l < r:
#             mid = r - (r - l) // 2
#             print(l,r,mid,count(mid))
#             if count(mid) >= m:
#                 l = mid
#             else:
#                 r = mid - 1
#         return l
    
"""
lo+hi = 10-20->30->15
hi-(hi-lo) = 20-(20-10) ->10->5
"""
        
            
            
        
        