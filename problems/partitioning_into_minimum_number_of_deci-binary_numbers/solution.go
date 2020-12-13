func max(a int, b int) int {
    if a>b {
        return a
    }
    return b
}

func minPartitions(n string) int {
    ans := 0
    for _,c := range n {
        val := int(c - '0')
        ans=max(ans,val)
    }
    return ans
}