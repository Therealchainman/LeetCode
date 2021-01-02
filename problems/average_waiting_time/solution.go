func averageWaitingTime(customers [][]int) float64 {
    time := customers[0][0]
    waitTime := 0
    for _, c := range customers {
        arriveTime := c[0]
        if time<c[0] {
            time = arriveTime + c[1]
        } else {
            time += c[1]
        }
        waitTime += time - arriveTime
    }
    avgWait := float64(waitTime)/float64(len(customers))
    return avgWait
}