class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha="abcdefghijklmnopqrstuvwxyz"[::-1]
        result=0
        for i in range(len(s)):
            a=alpha.index(s[i])+1
            b=i+1
            result+=(a*b)
        return result