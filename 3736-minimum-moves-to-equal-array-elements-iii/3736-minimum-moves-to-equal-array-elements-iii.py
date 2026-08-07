class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            if i <max(nums):
                result+=max(nums)-i
        return result
        