class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=s.count(s[0])
        b=set(s)
        for i in b:
            if s.count(i)!=a:
                return False
        return True
        
        