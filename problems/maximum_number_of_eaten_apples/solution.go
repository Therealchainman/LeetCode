type apple struct {
    numApples int
    numDays int
}

type RotHeap []apple

func (h RotHeap) Len() int           { return len(h) }
func (h RotHeap) Less(i, j int) bool { return h[i].numDays < h[j].numDays }
func (h RotHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *RotHeap) Push(x interface{}) {
    *h = append(*h, x.(apple))
}

func (h *RotHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}


func eatenApples(apples []int, days []int) int {
    h := &RotHeap{}
    n := len(apples)
    ans := 0
    var i int
    var a apple
    for i = 0;i<n;i++ {
        a = apple{apples[i], i+days[i]}
        heap.Push(h, a)
        for len(*h)>0 && (*h)[0].numDays<=i {
            heap.Pop(h)
        }
        if len(*h)>0 {
            if (*h)[0].numApples == 1 {
                heap.Pop(h)
            } else {
                (*h)[0].numApples--
            }
            ans++
        }

    }
    for len(*h)>0 {
        for len(*h)>0 && (*h)[0].numDays<=i {
            heap.Pop(h)
        }
        if len(*h)>0 {
            if (*h)[0].numApples == 1 {
                heap.Pop(h)
            } else {
                (*h)[0].numApples--
            }
            ans++
        }
        i++
    }
    return ans
}
