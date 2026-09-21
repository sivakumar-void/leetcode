class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        a=[x for x in arr if arr.count(x)==1]
        try:
            return a[k-1]
        except:
            return ""
        
        