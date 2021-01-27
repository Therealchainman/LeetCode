import (
    "container/heap"
)
type location struct {
    x int
    y int
}

type empty struct{}

type option struct {
    loc location
    priority int
}

type optionHeap []*option

func (h optionHeap) Len() int {return len(h)}
func (h optionHeap) Less(i, j int) bool {return h[i].priority < h[j].priority}
func (h optionHeap) Swap(i, j int) {h[i],h[j] = h[j],h[i]}

func (h *optionHeap) Push(x interface{}) {
    *h = append(*h, x.(*option))
}

func (h *optionHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

func minimumEffortPath(heights [][]int) int {
    R := len(heights)
    C := len(heights[0])
    pathHeap := &optionHeap{}
    vis := make(map[location]empty)
    dir := []location{location{1,0},location{0,1},location{-1,0},location{0,-1}}
    dist := make([][]int, R)
    for i, _ := range dist {
        e := make([]int, C)
        for j, _ := range e {
            e[j] = 1000000
        }
        dist[i] = e
    }
    pathData := &option{location{0,0},0}
    heap.Push(pathHeap,pathData)
    dist[0][0] = 0
    for pathHeap.Len() > 0 {
        path := heap.Pop(pathHeap).(*option)
        row := path.loc.x
        col := path.loc.y
        dist[row][col]=min(path.priority, dist[row][col])
        if _, found := vis[path.loc]; found {
            continue
        }
        vis[path.loc] = empty{}
        for _, nei := range dir {
            dx := nei.x
            dy := nei.y
            nx := row+dx
            ny := col+dy
            nloc := location{nx,ny}
            if nx>=0 && nx<R && ny>=0 && ny<C {
                diffHeights := max(path.priority, abs(heights[row][col] - heights[nx][ny]))
                pathData = &option{nloc,diffHeights}
                heap.Push(pathHeap, pathData)
            }
        }
    }
    return dist[R-1][C-1]
}
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
func max(x,y int) int {
    if x > y {
        return x
    }
    return y 
}
func min(x,y int) int {
    if x < y {
        return x
    }
    return y
}