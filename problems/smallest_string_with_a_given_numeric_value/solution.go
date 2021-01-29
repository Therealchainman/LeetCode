func getSmallestString(n int, k int) string {
    var b []byte
    for i:=n-1;i>0;i--{
        m := i*26
        if k <= m {
            b = append(b, 'a')
            k--
        } else {
            b = append(b, 'a' + byte(k-m-1))
            k -= (k - m)
        }
    }
    b = append(b, 'a'+byte(k-1))
    return string(b)
}