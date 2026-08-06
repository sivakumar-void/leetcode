class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=list(set(nums))
        
       
        for i in a:
            if nums.count(i)%2!=0:
                return False
                break
        return True

                
                
        return result
                
        