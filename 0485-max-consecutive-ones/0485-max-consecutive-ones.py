class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 if nums[0]==1 else 0
        else:
            a="".join(map(str,nums))
            result=[]
            for i in range(0,len(nums)+1):
                if "1"*i in a:
                    result.append(i)
                else:
                    break
            return max(result)
                
            
                
            
        
        
        



        