/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import 
    "container/heap"

type NodeHeap []*ListNode

func (h NodeHeap) Len() int {return len(h)}
func (h NodeHeap) Less(i, j int) bool {return h[i].Val < h[j].Val}
func (h NodeHeap) Swap(i, j int) {h[i],h[j] = h[j],h[i]}

func (h *NodeHeap) Push(x interface{}) {
    *h = append(*h, x.(*ListNode))
}

func (h *NodeHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    mergeHeap := &NodeHeap{}
    var head *ListNode
    var tail *ListNode
    var next *ListNode
    for _, ll := range lists {
        if ll != nil {
            heap.Push(mergeHeap, ll)
        }
    }
    
    for mergeHeap.Len()>0 {
        if tail != nil {
            next = heap.Pop(mergeHeap).(*ListNode)
            tail.Next = next
            if next.Next != nil {
                heap.Push(mergeHeap, next.Next)
            }
            tail=tail.Next
        } else {
            head = heap.Pop(mergeHeap).(*ListNode)
            tail = head
            if head.Next != nil {
                heap.Push(mergeHeap, head.Next)
            }
        }
    }
    return head
}