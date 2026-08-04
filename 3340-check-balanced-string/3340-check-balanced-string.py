class Solution:
    def isBalanced(self, num: str) -> bool:
        oddsum=[int(num[i]) for i in range(0,len(num),2)]
        evensum=[int(num[i]) for i in range(1,len(num),2)]
        return sum(oddsum)==sum(evensum)
        