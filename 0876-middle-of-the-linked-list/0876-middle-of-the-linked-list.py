# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        mid=(count//2)+1
        temp2=head
        i=1
        while i is not mid:
            temp2=temp2.next
            i+=1
        return temp2
        