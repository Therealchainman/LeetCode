class Solution:
    def findRightInterval(self, intervals):
        start_sorted=sorted((v[0],i) for i,v in enumerate(intervals))
        start_sorted+=[(float('inf'),len(intervals))]
        def possible(val,target):
            return start_sorted[val][0]>=target
        
        def binary_search(target):
            lo,hi=0,len(intervals)
            while lo < hi:
                mid = lo+hi>>1
                if not possible(mid,target):
                    lo=mid+1
                else:
                    hi=mid
            return lo
        ans=[]
        for s,e in intervals:
            left_index=binary_search(e)
            ans.append(start_sorted[left_index][1] if left_index<len(intervals) else -1)
        return ans
        