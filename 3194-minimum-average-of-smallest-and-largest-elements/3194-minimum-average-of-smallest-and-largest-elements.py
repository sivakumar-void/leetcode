class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        temp=nums
        avgs=[]
        for i in range(len(nums)):
            if len(temp)!=0:
                a=[max(temp),min(temp)]
                avgs.append(sum(a)/2)
                temp.remove(min(temp))
                temp.remove(max(temp))
            
        return min(avgs)

            
        