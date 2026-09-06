class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        alpha="abcdefghijklmnopqrstuvwxyz"
        ind=alpha.index(target)
        for i in range(ind+1,len(alpha)):
            if alpha[i] in letters:
                return alpha[i]
        return letters[0]
        

        