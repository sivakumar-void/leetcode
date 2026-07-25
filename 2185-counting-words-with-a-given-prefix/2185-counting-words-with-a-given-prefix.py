class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=0
        for i in range(len(words)):
            if words[i][:len(pref)]==pref:
                a+=1
        return a
            
    
        