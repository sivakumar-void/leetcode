class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result=[]
        n=len(nums)
        for i in range(n):
            
            if n%(i+1)==0 :
                result.append(nums[i]**2)
        return sum(result)
        