/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }
    var slow *ListNode = head
    var fast *ListNode = head
    for fast.Next != nil && fast.Next.Next != nil {
        slow=slow.Next
        fast=fast.Next.Next
        if (fast==slow) {
            return true
        }
    }
    return false
}