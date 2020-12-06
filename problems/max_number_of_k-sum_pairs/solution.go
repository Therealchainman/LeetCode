func maxOperations(nums []int, k int) int {
    sort.Ints(nums)
    n := len(nums)
    lo := 0
    hi := n - 1
    ans := 0
    for lo < hi {
        total := nums[lo]+nums[hi]
        if total == k {
            ans++
            hi--
            lo++
        } else if total < k {
            lo++
        } else {
            hi--
        }
    }
    return ans
}