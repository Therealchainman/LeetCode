func numberOfMatches(n int) int {
    ans := 0
    for n > 1 {
        if n%2==0 {
            ans += n/2;
            n/=2;
        } else {
            ans +=n/2;
            n=(n+1)/2;
        }
    }
    return ans
}