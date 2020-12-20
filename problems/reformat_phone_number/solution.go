func reformatNumber(number string) string {
    var res []string
    // Stores the digit
    for _,x := range number {
        if unicode.IsDigit(x) {
            res = append(res, string(x))
        }
    }
    n := len(res)
    ans := ""
    i := 0
    for n-i>4 {
        for j:=0;j<3;j++ {
            ans += res[i]
            i++
        }
        ans+="-"
    }
    if n-i==4 {
        for j:=0;j<2;j++ {
            ans+=res[i]
            i++
        }
        ans+="-"
        for j:=0;j<2;j++ {
            ans+=res[i]
            i++
        }
    } else if n-i==3 {
        for j:=0;j<3;j++ {
            ans+=res[i]
            i++
        }
    } else if n-i==2 {
        for j:=0;j<2;j++ {
            ans+=res[i]
            i++
        }
    }
    return ans
}