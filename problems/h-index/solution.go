func hIndex(A []int) int {
    var tot int
    var n int = len(A)
    counter := make([]int, len(A)+1)
    for _, a := range A {
        if a > n {
            counter[n]++
        } else {
            counter[a]++
        }
    }
    for i := n; i>=0;i-- {
        tot = tot + counter[i]
        if tot >= i {
            return i
        }
    }
    return 0
}