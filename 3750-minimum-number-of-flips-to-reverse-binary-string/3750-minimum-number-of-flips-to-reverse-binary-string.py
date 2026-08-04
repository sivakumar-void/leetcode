class Solution:
    def minimumFlips(self, n: int) -> int:
        given=bin(n)[2:]
        reverse=given[::-1]

        if given==reverse:
            return 0
        else:
            flips=0
            for i in range(len(given)):
                if given[i]!=reverse[i]:
                    flips+=1
            return flips

            

        
        