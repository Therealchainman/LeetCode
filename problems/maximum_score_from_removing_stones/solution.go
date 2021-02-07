
type IntHeap []int

func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i, j int) bool {return h[i] > h[j]}
func (h IntHeap) Swap(i, j int) {h[i],h[j] = h[j],h[i]}

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    var n = len(*h)
    var x = (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

func maximumScore(a int, b int, c int) int {
    var maxHeap = &IntHeap{a,b,c}
    var score = 0
    var x, y int
    for maxHeap.Len()>1 {
        x = heap.Pop(maxHeap).(int)
        y = heap.Pop(maxHeap).(int)
        x--
        y--
        if x>0 {
            heap.Push(maxHeap,x)
        }
        if y>0 {
            heap.Push(maxHeap,y)
        }
        score++
    }
    return score
}