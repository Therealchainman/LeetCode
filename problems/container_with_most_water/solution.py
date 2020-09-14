class Solution:
    def maxArea(self, H):
        for i,h in enumerate(H):
            H[i]=(h,i)
        H.sort(reverse=True)
        max_x=min_x=H[0][1]
        ret=0
        for hi,loc in H:
            max_dist=max(abs(max_x-loc),abs(min_x-loc))
            ret=max(ret,hi*(max_dist))
            max_x=max(max_x,loc)
            min_x=min(min_x,loc)
        return ret
        
        
"""
thoughts:

"""
        