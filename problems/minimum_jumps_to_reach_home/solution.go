func minimumJumps(forbidden []int, a int, b int, x int) int {
    forb := make(map[int]bool)
    for _, y := range forbidden {
        forb[y]=true
    }
    var queue [][3]int
    if _, found := forb[a]; found {
        return -1
    }
    var visited [5000]int
    visited[0]=1
    queue = append(queue, [3]int{0,1,0})
    for len(queue)>0 {
        cand := queue[0]
        loc := cand[0]
        steps := cand[2]
        flag := cand[1]
        if loc==x {
            return steps
        }
        queue[0]=[3]int{0,0,0}
        queue=queue[1:]
        backward := loc-b
        _, found := forb[backward]
        if flag==1 && !found && backward>=0 && visited[backward]==0 {
            queue=append(queue,[3]int{backward,0,steps+1})
            visited[backward]=1
        }
        forward := loc+a
        _, found = forb[forward]
        if !found && forward<5000 && visited[forward]==0 {
            queue=append(queue,[3]int{forward,1,steps+1})
            visited[forward]=1
        }
    }
    return -1
}