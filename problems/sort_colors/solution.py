class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(arr) - 1
        i = 0
        while i <= right:
            if arr[i] < 1:
                arr[i], arr[left] = arr[left], arr[i]
                i += 1
                left += 1
            elif arr[i] > 1:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            else:
                i += 1