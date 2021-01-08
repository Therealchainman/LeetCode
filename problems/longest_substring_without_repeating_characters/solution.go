func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
func lengthOfLongestSubstring(s string) int {
    count := make(map[byte]int)
    ans := 0
    le := 0
    ri := 0
    for ri<len(s) {
        count[s[ri]]++
        for count[s[ri]]>1 {
            count[s[le]]--
            le++
        }
        ans = max(ans, ri - le + 1)
        ri++
    }
    return ans
}