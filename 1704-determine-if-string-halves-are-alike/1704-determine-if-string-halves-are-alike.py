class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow="aeiou"
        a=s[:len(s)//2].lower()
        b=s[len(s)//2:].lower()
        x=0
        y=0
        for i in vow:
            x+=a.count(i)
            y+=b.count(i)
        return x==y



        