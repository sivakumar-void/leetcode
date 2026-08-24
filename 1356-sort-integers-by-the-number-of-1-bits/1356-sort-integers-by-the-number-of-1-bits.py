class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]: 
        arr.sort()
        from collections import defaultdict
        counts=defaultdict(list)
        for i in range(len(arr)):
            bi=bin(arr[i])
            ones=bi.count("1")
            counts[str(ones)].append(arr[i])
        order=list(set(map(int,counts.keys())))
        result=[]
        for j in order:
            result.extend(counts[str(j)])
        return result

        
        
         

        