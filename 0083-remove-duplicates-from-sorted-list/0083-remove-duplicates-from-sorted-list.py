# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        t1=head
        while t1:
            a.append(t1.val)
            t1=t1.next
        a=sorted(list(set(a)),reverse=True)
        head=None
        for i in a:
            new=ListNode(i)
            new.next=head
            head=new
        return head
        