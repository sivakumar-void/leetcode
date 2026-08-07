class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a=list(set(nums))
        cnt=0
        result=0
        for i in a:
            if nums.count(i)>cnt:
                cnt=nums.count(i)
                result=i
        return result
        