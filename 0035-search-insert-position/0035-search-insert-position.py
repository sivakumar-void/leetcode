class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target >nums[len(nums)-1]:
            return len(nums)
        elif target<nums[0] or len(nums)==1:
            return 0
        elif target in nums:
            return nums.index(target)
        
        else:
            for i in range(len(nums)-1):
                
                if nums[i]<target and nums[i+1]>target:
                    return i+1
                    break
                else:
                    continue



                


        
        
            


       
        