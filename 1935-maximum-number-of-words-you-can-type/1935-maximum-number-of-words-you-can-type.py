class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result=0
        for i in text.split():
            a=0
            for j in brokenLetters:
                if j in i:
                    a+=1
            if a==0:
                result+=1
        return result


        
        
                    
       
        