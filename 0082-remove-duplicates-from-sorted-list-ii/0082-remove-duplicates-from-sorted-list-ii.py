# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        b=[x for x in sorted(list(set(a))) if a.count(x)==1][::-1]
        head=None
        for i in b:
            new=ListNode(i)
            new.next=head
            head=new
        return head

        
            
            

        