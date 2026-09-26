# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        if len(a)<1:
            return head
        k=k%(len(a)*2)
        
        for i in range(k):
            a.insert(0,a[-1])
            a.pop()
        temp=head
        for i in a:
            temp.val=i
            temp=temp.next
        return head
            

        