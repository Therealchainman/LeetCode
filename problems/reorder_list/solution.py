# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow=head
        fast=slow.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur = slow.next
        stk=[]
        while cur:
            stk.append(cur)
            cur=cur.next
        cur=head
        while stk:
            stk[-1].next=cur.next
            cur.next=stk.pop()
            cur=cur.next.next
        cur.next=None
            