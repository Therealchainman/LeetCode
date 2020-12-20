func max(a, b int) int {
    if a>b{
        return a
    }
    return b
}

func maximumUniqueSubarray(nums []int) int {
    count := make(map[int]int)
    le := 0
    ri := 0
    ans := 0
    sum := 0
    n := len(nums)
    for ri<n {
        sum+=nums[ri]
        count[nums[ri]]++
        for count[nums[ri]]>1 {
            sum-=nums[le]
            count[nums[le]]--
            le++
        }
        ans = max(sum, ans)
        ri++
    }
    return ans
}