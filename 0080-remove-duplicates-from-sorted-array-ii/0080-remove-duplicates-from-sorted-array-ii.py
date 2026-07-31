class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=sorted(list(set(nums)))
        result=[]
        
        for i in a:
            if nums.count(i)==2 or nums.count(i)>2:
                result.extend([i,i])
            else:
                result.append(i)
        nums[:]=result
            
                
                
        