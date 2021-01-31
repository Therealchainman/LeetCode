func isPalindrome(s string, start int, end int) bool {
    for start < end {
        if s[start]!=s[end] {
            return false
        }
        start++
        end--
    }
    return true
}
func checkPartitioning(s string) bool {
    start := 0
    n := len(s)
    for i:=0;i<3;i++ {
        for end:=n-1;end>=start;end-- {
            if isPalindrome(s, start, end) {
                start = end+1
                break
            }
        }
    }
    return start == n
}