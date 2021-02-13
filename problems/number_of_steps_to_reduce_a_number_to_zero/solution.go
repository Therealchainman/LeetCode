func numberOfSteps (num int) int {
    var steps = 0
    for num > 0 {
        steps++
        if num%2 == 0 {
            num/=2
        } else {
            num--
        }
    }
    return steps
}