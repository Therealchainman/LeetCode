type IntHeap []int

func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i int, j int) bool {return h[i] < h[j]}
func (h IntHeap) Swap(i int, j int) {h[i], h[j] = h[j], h[i]}

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func min(a int, b int ) int {
    if a < b {return a}
    return b
}

func minimumDeviation(nums []int) int {
    h := &IntHeap{}
    lo := math.MaxInt64
    for i:=0;i<len(nums);i++ {
        if nums[i] & 1 == 1 {
            nums[i] = 2*nums[i]
        }
        lo = min(lo, nums[i])
        heap.Push(h, -nums[i])
    }
    ret := math.MaxInt64
    for true {
        hi := -heap.Pop(h).(int)
        ret = min(ret, hi-lo)
        if hi & 1 == 1 {
            break
        }
        hi/=2
        lo = min(lo, hi)
        heap.Push(h, -hi)
    }
    return ret
}