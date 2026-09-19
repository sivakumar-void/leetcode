# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        a=[]
        for head in lists:
            t=head
            while t:
                a.append(t.val)
                t=t.next
        a=sorted(a,reverse=True)
        lists=None
        for i in a:
            new=ListNode(i)
            new.next=lists
            lists=new
        return lists


        