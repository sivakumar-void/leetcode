class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x=bin(n)[2:]
        y = x.translate(str.maketrans("01", "10"))
        return int(y,2)