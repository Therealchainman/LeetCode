class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        A=nums[n-k:]+nums[:n-k]
        for i,a in enumerate(A):
            nums[i]=a