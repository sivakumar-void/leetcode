class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        for i in matrix:
            result.append(i.count(1))
        return result
        