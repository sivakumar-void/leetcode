class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=[]
        for i in nums:
            if i!= val:
                a.append(i)
        nums[:]=a
        
            

        

        
        
        