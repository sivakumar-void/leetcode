# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        t=head
        a=[]
        while t:
            a.append(t.val)
            t=t.next
        
        a=[x for x in a if x!=val][::-1]
        head=None
        for i in a:
            n=ListNode(i)
            n.next=head
            head=n
        return head



            


            
        
        