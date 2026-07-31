class Solution:
    def maxDistinct(self, s: str) -> int:
        a=list(set(i for i in s))
        return len(a)
        


            
        