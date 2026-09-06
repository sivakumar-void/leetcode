class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.lower()==word or word.upper()==word or word==word[0].upper()+word[1::].lower() else False
        
        