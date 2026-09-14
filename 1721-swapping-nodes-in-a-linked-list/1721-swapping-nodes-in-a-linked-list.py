# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        l=k-1
        r=len(a)-k
        a[l],a[r]=a[r],a[l]
        temp=head
        for i in a:
            temp.val=i
            temp=temp.next
        return head
        