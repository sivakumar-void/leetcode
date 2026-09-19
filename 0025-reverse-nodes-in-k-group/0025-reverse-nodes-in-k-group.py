# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        l1=[]
        t=head
        while t:
            l1.append(t.val)
            t=t.next
        l2=[]
        for i in range(k-1,len(l1),k):
            l2.extend(l1[i-(k-1):i+1][::-1])
        temp=head
        for i in l2:
            temp.val=i
            temp=temp.next
        return head


        
        