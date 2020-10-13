# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        A=[]
        while head:
            A.append(head.val)
            head=head.next
        A.sort()
        front=ListNode(None)
        cur=front
        for x in A:
            cur.next=ListNode(x)
            cur=cur.next
        return front.next