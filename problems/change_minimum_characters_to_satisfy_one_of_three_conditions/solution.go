func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func minCharacters(a string, b string) int {
    afreq := make(map[int]int)
    bfreq := make(map[int]int)
    freq := make(map[int]int)
    gfreq := 0
    total := 0
    for _, ch := range a {
        afreq[int(ch-'a')]++
        freq[int(ch-'a')]++
        total++
    }
    for _, ch := range b {
        bfreq[int(ch-'a')]++
        freq[int(ch-'a')]++
        total++
    }
    for _, f := range freq {
        gfreq = max(f,gfreq)
    }
    ans := total-gfreq
    for i:=1;i<26;i++ {
        cost := 0
        cost2 := 0
        for ch, f := range afreq {
            if ch >= i {
                cost+=f
            }
            if ch < i {
                cost2+=f
            }
        }
        for ch, f := range bfreq {
            if ch < i {
                cost+=f
            }
            if ch >= i {
                cost2+=f
            }
        }
        ans=min(ans,cost)
        ans=min(ans,cost2)
    }
    return ans
}