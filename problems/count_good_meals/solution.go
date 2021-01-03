func countPairs(deliciousness []int) int {
    mod := int(1e9)+7
    ans := 0
    seen := make(map[int]int)
    for _, d := range deliciousness {
        seen[d]++
    }
    for i:=0;i<=21;i++{
        cand := int(math.Pow(2,float64(i)))
        for _, d := range deliciousness {
            cnt := seen[cand-d]
            if cnt>0 && cand!=2*d {
                ans+=cnt
            } else if cnt>0  {
                ans+=(cnt-1)
            }
        }
    }
    return (ans/2)%mod
}