class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result=[]
        for i in range(len(A)):
            a=list(set(A[:i+1]).intersection(set(B[:i+1])))
            if a==[]:
                result.append(0)
            else:
                result.append(len(a))
        return result

            
        
        