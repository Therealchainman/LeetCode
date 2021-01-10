/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func swapNodes(head *ListNode, k int) *ListNode {
    n := 0
    cur := head
    for (cur!=nil) {
        n++
        cur=cur.Next
    }
    front := &ListNode{0,head}
    head = nil
    c := front.Next
    var first int
    var second int
    for i:=0;i<n;i++ {
        if i==k-1 {
            first = c.Val
        }
        if i==n-k {
            second = c.Val
        }
        c=c.Next
    }
    b := front
    for i:=0;i<n+1;i++ {
        if i==k-1 {
            b.Next=&ListNode{second,b.Next.Next}
        }
        if i==n-k {
            b.Next=&ListNode{first,b.Next.Next}
        }
        b=b.Next
    }
    return front.Next
}

// func bToMb(b uint64) uint64 {
//     return b / 1024 / 1024
// }

// func PrintMemUsage() {
//         var m runtime.MemStats
//         runtime.ReadMemStats(&m)
//         // For info on each, see: https://golang.org/pkg/runtime/#MemStats
//         fmt.Printf("Alloc = %v MiB", bToMb(m.Alloc))
//         fmt.Printf("\tTotalAlloc = %v MiB", bToMb(m.TotalAlloc))
//         fmt.Printf("\tSys = %v MiB", bToMb(m.Sys))
//         fmt.Printf("\tNumGC = %v\n", m.NumGC)
// }