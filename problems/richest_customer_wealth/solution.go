func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}
func maximumWealth(accounts [][]int) int {
    ans := 0
    for i:=0;i<len(accounts);i++ {
        s := 0
        for j:=0;j<len(accounts[i]);j++ {
            s+=accounts[i][j]
        }
        ans = max(ans,s)
    }
    return ans
}