# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        a=[]
        t=head
        while t:
            a.append(t.val)
            t=t.next
        b=[]
        for i in range(len(a)):
            if b==[] or a[i]==0:
                b.append(0)
            else:
                b[-1]+=a[i]
        b.pop()
        b=b[::-1]
        head=None
        for i in b:
            new=ListNode(i)
            new.next=head
            head=new
        return head

        