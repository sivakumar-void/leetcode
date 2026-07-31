class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            check = 0
            for j in range(len(s)):
                if(i == j):
                    continue
                if(s[i] == s[j]):
                    check = 1
                    break
            if(check == 0):
                return i
        return -1