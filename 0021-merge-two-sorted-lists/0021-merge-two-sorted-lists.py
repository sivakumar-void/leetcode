# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None :
            return list2
        if list2 is None:
            return list1
        t1=list1
        t2=list2
        a=[]
        b=[]
        while t1:
            a.append(t1.val)
            t1=t1.next
        while t2:
            b.append(t2.val)
            t2=t2.next
        c = sorted(a + b)

        temp = list1

        for i in range(len(c)):
            if temp is None:
        # Need previous node to connect new node
                prev.next = ListNode(c[i])
                temp = prev.next
            else:
                temp.val = c[i]

            prev = temp
            temp = temp.next

        return list1


        
        

        
        