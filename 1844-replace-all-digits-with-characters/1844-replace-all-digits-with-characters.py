class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        ptr1=0
        ptr2=1
        result=""
        while ptr2<len(s):
            result+=s[ptr1]+alpha[alpha.index(s[ptr1])+int(s[ptr2])]
            ptr1+=2
            ptr2+=2
        return result if len(s)%2==0 else result+s[len(s)-1]
        