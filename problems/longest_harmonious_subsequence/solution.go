func findLHS(nums []int) int {
    mx := -int(1e10)
    mn := int(1e10)
    count := make(map[int]int)
    for _, x := range nums {
        mx = max(mx, x)
        mn = min(mn, x)
        count[x]++
    }
    ans := 0
    for i, cnt := range count {
        cur := cnt + count[i+1]
        if count[i+1]>=1 {ans = max(ans, cur)}
    }
    return ans
}

func max(x ,y int) int {
    if x > y {return x}
    return y
}

func min(x, y int) int {
    if x < y {return x}
    return y
}