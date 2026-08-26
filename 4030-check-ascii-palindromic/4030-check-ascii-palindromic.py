class Solution:
    def isPalindromic(self, s: str) -> bool:
        pal=""
        for i in s:
            pal+=str(format(ord(i),"08b"))
        return pal==pal[::-1]
        