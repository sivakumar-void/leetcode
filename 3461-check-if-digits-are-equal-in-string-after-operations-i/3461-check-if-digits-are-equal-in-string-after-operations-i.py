class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s)==2:
            return s[0]==s[1]
        else:
            result=[(int(s[i])+int(s[i+1]))%10 for i in range(len(s)-1)]
            while len(result)>2:
                result=[(int(result[i])+int(result[i+1]))%10 for i in range(len(result)-1)]
            return result[0]==result[1]

            

        
        