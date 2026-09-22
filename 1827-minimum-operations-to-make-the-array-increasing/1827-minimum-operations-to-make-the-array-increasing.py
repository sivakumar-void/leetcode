class Solution:
    def minOperations(self, nums: List[int]) -> int:
        current=0
        ops=0
        for i in nums:
            if current<i:
                current=i
            else:
                j=current
                current=current+1
                ops+=current-i
        return ops
        
        
        