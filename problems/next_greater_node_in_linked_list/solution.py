# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        stk=[]
        while head:
            stk.append(head)
            head=head.next
        ret=[]
        prev=[]
        while stk:
            head=stk.pop()
            while prev and prev[-1].val<=head.val:
                prev.pop()
                
            if not prev:
                ret.append(0)
                prev.append(head)
                continue
            ret.append(prev[-1].val)
            prev.append(head)
        ret.reverse()
        return ret
            
        
"""

"""
        