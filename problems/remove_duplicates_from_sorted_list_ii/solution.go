/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    var nums []int
    count := make(map[int]int)
    for head!=nil {
        count[head.Val]++
        if count[head.Val]==1 {
            nums = append(nums,head.Val)
        }
        head=head.Next
    }
    cur := &ListNode{}
    front := cur
    for _, val := range nums {
        if count[val]==1 {
            cur.Next = &ListNode{val,nil}
            cur=cur.Next
        }
    }
    return front.Next
}

/*
  1    2    3   4
[ x ] [  ] [  ] [  ]
variable node equal to memory address 1

*/