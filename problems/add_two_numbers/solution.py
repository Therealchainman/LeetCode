# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1,l2):
        s=["",""]
        
        for i,cur in enumerate([l1,l2]):
            while cur:
                s[i]+=f"{cur.val}"
                cur=cur.next
        tot=int(s[0][::-1])+int(s[1][::-1])
        tot=str(tot)[::-1]
        print(tot)
        front=cur=ListNode(None)
        for s in tot:
            cur.next=ListNode(int(s))
            cur=cur.next
        return front.next
        