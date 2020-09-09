class Solution:
    def searchRange(self, nums,target):
        def possible(val,target,pos):
            return val>=target if pos=="first" else val<=target
        n=len(nums)
        def binary_search(pos):
            lo,hi=0,n-1
            if pos=="first":
                while lo<hi:
                    mid=lo+hi>>1
                    if not possible(nums[mid],target,pos):
                        lo=mid+1
                    else:
                        hi=mid
            else:
                while lo<hi:
                    mid=lo+hi+1>>1
                    if possible(nums[mid],target,pos):
                        lo=mid
                    else:
                        hi=mid-1
            return lo
        idx_first,idx_last=binary_search("first"),binary_search("last")
        return [idx_first,idx_last] if nums and nums[idx_first]==target else [-1,-1]
            