func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func maxPower(s string) int {
    var count =1
    var ans = 1
    for i:=1;i<len(s);i++ {
        if s[i]==s[i-1] {
            count++
        } else {
            count=1
        }
        ans=max(ans,count)
    }
    return ans
}