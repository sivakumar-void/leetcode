class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c=0
        a=len(nums)
        for i in range(a):
            for j in range(i+1,a):
                for k in range(j+1,a):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        c+=1
        return c

        
        