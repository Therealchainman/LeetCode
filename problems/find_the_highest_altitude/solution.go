func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
func largestAltitude(gain []int) int {
    curAltitude := 0
    highestAltitude := 0
    for _, g := range gain {
        curAltitude += g
        highestAltitude = max(curAltitude, highestAltitude)
    }
    return highestAltitude
}