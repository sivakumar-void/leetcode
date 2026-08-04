class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        left=0
        right=len(s)-1
        result=-1
        while left<right:
            if s[left]==s[right]:
                result=left
                break
            left+=1
            right-=1
        return len(s)//2 if (len(s)%2 != 0 and result == -1) else result

            
        