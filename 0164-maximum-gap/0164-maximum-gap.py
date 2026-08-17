class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxgap=0
        for i in range(len(nums)-1):
            if maxgap<nums[i+1]-nums[i]:
                maxgap=nums[i+1]-nums[i]
        return maxgap


        
            
        
            
        
        