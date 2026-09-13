# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        head=None
        for i in a:
            new=ListNode(i)
            new.next=head
            head=new
        return head
        



       
        