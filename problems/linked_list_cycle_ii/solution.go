/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    var i = 0
    nodes := make(map[*int]int)
    for head != nil {
        if _, found := nodes[&head.Val]; found {
            return head
        }
        nodes[&head.Val]=i
        head=head.Next
        i++
    }
    return nil
}