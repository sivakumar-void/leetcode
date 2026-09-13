# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        a=a[:left-1]+a[left-1:right][::-1]+a[right:]
        temp=head
        for i in a:
            temp.val=i
            temp=temp.next
        return head



        