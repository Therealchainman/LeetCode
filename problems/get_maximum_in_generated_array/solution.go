func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func getMaximumGenerated(n int) int {
    nums := make([]int, n+1)
    if n==0 {
        return 0
    }
    ans := 1
    nums[0]=0
    nums[1]=1
    for i:=2;i<=n;i++ {
        if i%2==0 {
            nums[i]=nums[i/2]
        } else {
            nums[i]=nums[i/2]+nums[i/2+1]
        }
        ans = max(ans, nums[i])
    }
    return ans
}