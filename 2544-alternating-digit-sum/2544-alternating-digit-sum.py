class Solution:
    def alternateDigitSum(self, n: int) -> int:
        odds=[int(str(n)[i]) for i in range(len(str(n))) if i%2==0]
        evens=[-int(str(n)[j]) for j in range(len(str(n))) if j%2!=0]
        return sum(odds)+sum(evens)


        