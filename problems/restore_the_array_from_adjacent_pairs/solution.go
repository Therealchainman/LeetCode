type empty struct {}

func restoreArray(adjacentPairs [][]int) []int {
    graph := make(map[int][]int)
    vis := make(map[int]empty)
    cnt := make(map[int]int)
    var x int
    var y int
    for _, pair := range adjacentPairs {
        x = pair[0]
        y = pair[1]
        graph[x] = append(graph[x], y)
        graph[y] = append(graph[y], x)
        cnt[x]++
        cnt[y]++
    }
    start := int(1e9)
    for val, cnt := range cnt {
        if cnt == 1 && start > 10000 {
            start = val
        }
    }

    nums := make([]int,len(cnt))
    for i:=0;i<len(nums);i++ {
        nums[i] = start
        vis[start] = empty{}
        for _, x := range graph[start] {
            if _, found := vis[x]; !found {
                start = x
            }
        }
    }
    return nums
}