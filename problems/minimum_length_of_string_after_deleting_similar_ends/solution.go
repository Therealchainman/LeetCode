func minimumLength(s string) int {
    var n = len(s)
    var left = 0
    var right = n-1
    for left < right && s[left]==s[right] {
        var ch = s[left]
        for left<n && s[left]==ch{
            left++
        }
        for right>=0 && s[right]==ch{
            right--
        }
        if left>right{
            return 0
        }
    }
    return right-left+1
}