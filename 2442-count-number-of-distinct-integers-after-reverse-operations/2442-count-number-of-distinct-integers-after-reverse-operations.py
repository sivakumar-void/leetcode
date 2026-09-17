class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=nums+[int(str(i)[::-1]) for i in nums]
        return len(set(a))
        