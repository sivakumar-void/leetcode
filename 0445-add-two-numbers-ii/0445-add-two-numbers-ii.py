# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b="",""
        t1,t2=l1,l2
        while t1:
            a+=str(t1.val)
            t1=t1.next
        while t2:
            b+=str(t2.val)
            t2=t2.next
        head=None
        for i in str(int(a)+int(b))[::-1]:
            new=ListNode(int(i))
            new.next=head
            head=new
        return head
            
        