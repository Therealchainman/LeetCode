# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        cur=head
        x=1
        while cur.next:
            x+=1
            cur=cur.next
        if k==0 or x==k:
            return head
        cur.next=head
        k%=x
        temp=cur.next
        for _ in range(x-k-1):
            temp=temp.next
        ans=temp.next
        temp.next=None
        return ans
        
            
            