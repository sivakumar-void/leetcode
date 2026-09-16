class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        a=[]
        b=[i for i in range(1,n+1)]
        for i in combinations(b,k):
            a.append(list(i))
        return a
        
        
        