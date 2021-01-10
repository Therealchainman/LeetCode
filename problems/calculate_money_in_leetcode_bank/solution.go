func totalMoney(n int) int {
    gross := 0
    base := 1
    for n>0 {
        for day:=0;day<7;day++ {
            if n==0 {
                break
            }
            gross += base+day
            n--
        }
        base++
    }
    return gross
}