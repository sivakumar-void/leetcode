class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=[i for i in nums if i>=k]
        return len(nums)-len(a)
        