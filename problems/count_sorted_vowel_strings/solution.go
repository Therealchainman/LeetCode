func countVowelStrings(n int) int {
    var prefix = []int{1,2,3,4,5}
    if n==1 {
        return 5
    }
    for i := 2;i<=n;i++ {
        for j := 1;j<5;j++ {
            prefix[j]+=prefix[j-1]
        }
    }
    return prefix[4]
}