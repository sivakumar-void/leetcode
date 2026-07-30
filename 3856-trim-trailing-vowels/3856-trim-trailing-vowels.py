class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vow="aeiou"
        result=[i for i in s]
        for i in range(len(s)):
            if result[len(result)-1] in vow:
                result.pop()
            else:
                break
        return "".join(result)

                
                
        