class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1) if len(word1) <len(word2) else len(word2)
        result=""
        b=word1 if len(word1) >len(word2) else word2
        for i in range(a):
            result+=word1[i]
            result+=word2[i]
        return result+b[a:]
        
            

        