class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        from collections import defaultdict
        d=defaultdict(str)
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            d[alpha[i]]=morse[i]
        result=[]
        for j in words:
            temp=""
            for k in j:
                temp+=d[k]
            result.append(temp)
        return len(set(result))
        
            
        

        

        