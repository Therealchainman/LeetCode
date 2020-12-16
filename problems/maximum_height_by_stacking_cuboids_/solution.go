func max(a, b int) int {
    if a>b {
        return a
    }
    return b
}

func maxHeight(cuboids [][]int) int {
    n := len(cuboids)
    dp := make([]int,n)
    for i:=0;i<n;i++ {
        sort.Ints(cuboids[i])
    }
    sort.SliceStable(cuboids, func(i, j int) bool {
        if cuboids[i][2] != cuboids[j][2] {
            return cuboids[i][2]<cuboids[j][2]
        }
        if cuboids[i][1] != cuboids[j][1] {
            return cuboids[i][1]<cuboids[j][1]
        }
        return cuboids[i][0]<cuboids[j][0]
    })
    ans := 0
    for i:=0;i<n;i++ {
        dp[i]=cuboids[i][2]
        ans = max(ans,dp[i])
    }
    for i:=0;i<n;i++ {
        for j:=0;j<i;j++ {
            if cuboids[i][0]>=cuboids[j][0] && cuboids[i][1] >= cuboids[j][1] && cuboids[i][2]>=cuboids[j][2] {
                dp[i] = max(dp[i],dp[j]+cuboids[i][2])
            }
            ans = max(ans,dp[i])
        }
    }
    return ans
}