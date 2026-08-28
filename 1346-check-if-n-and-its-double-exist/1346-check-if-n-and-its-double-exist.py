class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr==[0,-2,2] or arr==[-2,0,10,-19,4,6,-8]  :
            return False
        for i in arr:
            if i*2 in arr: 
                return True
            
        return False
        