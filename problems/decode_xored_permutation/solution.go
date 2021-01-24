func decode(encoded []int) []int {
    start := 0
    for i:=1;i<len(encoded)+2;i++ {
        start^=i
    }
    cur := 0
    for _, x := range encoded {
        cur^=x
        start^=cur
    }
    ans := []int{start}
    for i:=0;i<len(encoded);i++{
        ans = append(ans, ans[len(ans)-1]^encoded[i])
    }
    return ans
}