func binarySearch(nums []int) int {
    lo, hi := 0, len(nums)-1
    for lo<hi{
        mi := (lo+hi+1)>>1
        if mi>0 && nums[mi-1]<nums[mi] {
            lo = mi
        } else {
            hi=mi-1
        }
    }
    return lo
}
func findPeakElement(nums []int) int {
    return binarySearch(nums)
}