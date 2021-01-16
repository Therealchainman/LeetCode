func findKthLargest(nums []int, k int) int {
    sort.Ints(nums)
    n := len(nums)
    for i:=n-1;i>=0;i-- {
        k--
        if k==0 {
            return nums[i]
        }
    }
    return 0
}