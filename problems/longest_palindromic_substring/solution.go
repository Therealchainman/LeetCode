func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func expand(s string, i, j int) string {
    for i >= 0 && j < len(s) {
        if s[j]!=s[i] {
            break
        }
        i--
        j++
    }
    return s[i+1:j]
}

func longestPalindrome(s string) string {
    n := len(s)
    longest := ""
    high := 0
    var oddPalindrome string
    var evenPalindrome string
    for i:=0;i<n;i++ {
        oddPalindrome = expand(s,i,i)
        if len(oddPalindrome) > high {
            longest = oddPalindrome
            high = len(oddPalindrome)
        }
        if i>0 && s[i-1]==s[i] {
            evenPalindrome = expand(s,i-1,i)
            if len(evenPalindrome) > high {
                longest = evenPalindrome
                high = len(evenPalindrome)
            }
        }
    }
    return longest
}