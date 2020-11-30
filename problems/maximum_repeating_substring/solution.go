func mod(a int, b int) int {
    return (a % b + b) % b;
}
func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}
func maxRepeating(sequence string, word string) int {
    ans := 0
    j := 0
    i := 0
    for i<len(sequence) {
        if sequence[i]==word[mod(j,len(word))] {
            j++
        } else {
            i-=max(mod(j,len(word))-1,0)
            j=0
            if sequence[i]==word[mod(j,len(word))] {
                j++
            }
        }
        i++
        ans=max(ans,j/len(word))
    }
    return ans
}