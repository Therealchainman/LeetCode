func decode(encoded []int, first int) []int {
    var ans []int
    ans = append(ans, first)
    cur := first
    for _, x := range encoded {
        cur = x^cur
        ans = append(ans, cur)
    }
    return ans
}