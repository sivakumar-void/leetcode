# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=0
        b=[]
        t=head
        while t:
            a+=1
            b.append(t.val)
            t=t.next
        a=(a//2)
        del b[a]
        b=b[::-1]
        head=None
        for i in b:
            new=ListNode(i)
            new.next=head
            head=new
        return head
        
        
        