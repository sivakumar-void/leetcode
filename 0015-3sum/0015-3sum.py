class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        if len(nums)<3:
            return []
        for i in range(len(nums)-2):
            if nums[i-1]==nums[i] and i>0:
                continue
            ref=nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                sum3=ref+nums[left]+nums[right]
                if sum3==0:
                    result.append([ref,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right]==nums[right+1] and left <right:
                        right-=1
                elif sum3<0:
                    left+=1
                    while nums[left]==nums[left-1] and left <right:
                        left+=1
                else:
                    right-=1
                    while nums[right]==nums[right+1] and left < right:
                        right-=1
        return result

                
                    
        
            


        
        
        