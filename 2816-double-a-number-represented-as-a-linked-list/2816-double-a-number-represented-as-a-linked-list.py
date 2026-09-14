# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.set_int_max_str_digits(10000)

        a=""
        temp1=head
        while temp1:
            a+=str(temp1.val)
            temp1=temp1.next
        b=str(int(a)*2)[::-1]
        head=None
        for i in b:
            new=ListNode(int(i))
            new.next=head
            head=new
        return head
        
        
        