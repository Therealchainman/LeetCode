func min(x, y int) int {
    if x<y {
        return x
    }
    return y
}
func maximumUnits(boxTypes [][]int, truckSize int) int {
    sort.SliceStable(boxTypes, func(i, j int) bool {
        return boxTypes[i][1] > boxTypes[j][1]
    }) 
    i:=0
    ans:=0
    for i<len(boxTypes) && truckSize>0 {
        take:=min(boxTypes[i][0],truckSize)
        ans+=(take*boxTypes[i][1])
        truckSize-=take
        i++
    }
    return ans
}