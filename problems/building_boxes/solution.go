func minimumBoxes(n int) int {
    var cnt, i, j = 0, 0, 0
    for cnt < n {
        j++
        i+=j
        cnt+=i
    }
    if cnt == n {
        return i
    }
    cnt-=i
    i-=j
    j=0
    for cnt < n {
        j++
        cnt+=j
    }
    return i + j
}