class Solution:
    def trailingZeroes(self, n: int) -> int:
        import sys

        sys.set_int_max_str_digits(1000000)
        import math as m
        fact=str(math.factorial(n))[::-1]
        count=0
        for i in fact:
            if i!="0":
                break
            count+=1
        return count
        