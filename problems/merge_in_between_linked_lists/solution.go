/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
    LL := list1
    for list1.Next.Val != a {
        list1=list1.Next
    }
    firstCut := list1
    for list1.Val != b {
        list1=list1.Next
    }
    firstCut.Next=list2
    for list2.Next != nil {
        list2=list2.Next
    }
    list2.Next=list1.Next
    return LL
}