import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        a = []
        t = head

        while t:
            a.append(t.val)
            t = t.next

        if len(a) < 2:
            return head

        b = []

        for i in range(len(a) - 1):
            b.append(a[i])
            b.append(math.gcd(a[i], a[i + 1]))

        b.append(a[-1])

        head = None

        for i in b[::-1]:
            new = ListNode(i)
            new.next = head
            head = new

        return head
        
        
        