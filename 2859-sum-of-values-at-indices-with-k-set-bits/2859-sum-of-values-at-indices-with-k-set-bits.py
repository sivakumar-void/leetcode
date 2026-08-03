class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a=[nums[i] for i in range(len(nums)) if bin(i).count("1")==k]
        return sum(a)
        