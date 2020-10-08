class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def possible(val,target):
            return val<=target
        def binary_search(target):
            lo,hi=0,n-1
            while lo<hi:
                mid=hi+lo+1>>1
                if possible(nums[mid],target):
                    lo=mid
                else:
                    hi=mid-1
            return lo
        x=binary_search(target)
        print(x)
        return x if nums[x]==target else -1