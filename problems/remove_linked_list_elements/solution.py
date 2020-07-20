# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        currNode = dummy
        while currNode.next:
            print(currNode.next.val)
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return dummy.next

"""
5 -> 

6 -> 6 -> 6 -> 

"""