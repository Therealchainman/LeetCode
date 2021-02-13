import "math/bits"
func numberOfSteps (num int) int {
    if num==0{return 0}
    u := uint(num)
    return bits.UintSize - bits.LeadingZeros(u) + bits.OnesCount(u) - 1
}