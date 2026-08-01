class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result=nums
        for i in range(k):
            a=min(result)
            result[result.index(a)]=a*multiplier
        return result

        