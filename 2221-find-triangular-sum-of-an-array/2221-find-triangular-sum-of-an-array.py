class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        result=[(nums[i]+nums[i+1]) if (nums[i]+nums[i+1])<10 else (nums[i]+nums[i+1])-10 for i in range(len(nums)-1)]
        while len(result)>1:
            result=[(result[i]+result[i+1]) if (result[i]+result[i+1])<10 else (result[i]+result[i+1])-10 for i in range(len(result)-1)]
        return result[0]
        