class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=str(num)[::-1]
        b=str(int(a))[::-1]
        return str(num)==b
        