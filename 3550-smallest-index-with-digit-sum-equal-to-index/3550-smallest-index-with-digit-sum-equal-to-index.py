class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        result=-1
        for i in range(len(nums)):
            a=[int(i) for i in str(nums[i])]
            if sum(a)==i:
                result=i
                break
        return result


        
        