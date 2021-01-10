func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    graph := make(map[int][]int)
    for _, x := range allowedSwaps {
        graph[x[0]] = append(graph[x[0]], x[1])
        graph[x[1]] = append(graph[x[1]], x[0])
    }
    ans:=0
    visited := make(map[int]bool)
    for i:=0;i<len(source);i++ {
        if visited[i] {
            continue
        }
        count := make(map[int]int)
        var q []int
        q = append(q, i)
        seen := q
        for len(q)>0 {
            visited[i]=true
            j := q[0]
            q = q[1:]
            for _, next := range graph[j] {
                if !visited[next] {
                    q = append(q, next)
                    seen = append(seen, next)
                    visited[next]=true
                }
            }
        }
        for _, v := range seen {
            count[source[v]]++
            count[target[v]]--
        }
        for _, c := range count {
            if c > 0 {
                ans+=c
            }
        }
        
    }
    return ans
}