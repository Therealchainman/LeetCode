func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func sum(x int) int {
    res := 0
    for x > 0 {
        res += (x%10)
        x/=10
    }
    return res
}

func countBalls(lowLimit int, highLimit int) int {
    count := make(map[int]int)
    for i:=lowLimit;i<=highLimit;i++{
        count[sum(i)]++
    }
    ans := 0
    for _, cnt := range count {
        ans = max(ans, cnt)
    }
    return ans
}