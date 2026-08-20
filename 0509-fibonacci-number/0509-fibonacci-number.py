class Solution:
    def fib(self, n: int) -> int:
        a=[0,1]
        if n<2:
            return a[n]
        else:
            for i in range(n-1):
                a.append(a[-2]+a[-1])
            return a[-1]
        
        
        