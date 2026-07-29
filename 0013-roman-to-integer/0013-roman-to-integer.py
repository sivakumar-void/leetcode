class Solution:
    def romanToInt(self, s: str) -> int:
        vals={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)-1):
            if vals[s[i]]>=vals[s[i+1]]:
                result+=vals[s[i]]
            else:
                result-=vals[s[i]]
        result+=vals[s[-1]]
        return result

        