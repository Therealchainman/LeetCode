type pair struct {
    num int
    limit int
}

type minHeap []*pair

func (h minHeap) Len() int {return len(h)}
func (h minHeap) Less(i, j int) bool {return h[i].num < h[j].num}
func (h minHeap) Swap(i, j int) {h[i],h[j]=h[j],h[i]}

func (h *minHeap) Push(x interface{}) {
    *h = append(*h, x.(*pair))
}

func (h *minHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}


func minimumDeviation(nums []int) int {
    minHeap := &minHeap{}
    var mx int
    for _, n := range nums {
        tmp := n
        for tmp%2==0 {
            tmp/=2
        }
        heap.Push(minHeap,&pair{tmp,max(n,tmp*2)})
        mx = max(mx, tmp)
    }
    var p *pair
    ans := int(1e9)
    for minHeap.Len() == len(nums) {
        p = heap.Pop(minHeap).(*pair)
        ans = min(ans, mx - p.num)
        if p.num < p.limit {
            p.num*=2
            heap.Push(minHeap,p)
            mx = max(mx, p.num)
        }
    }
    
    return ans
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}