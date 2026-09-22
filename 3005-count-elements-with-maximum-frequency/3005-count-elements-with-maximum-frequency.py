class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=list(set(nums))
        maxfreq=0
        result=0

        for i in a:
            c=nums.count(i)
            if c>maxfreq:
                maxfreq=c
                result=c
            elif c==maxfreq:
                result+=c
            else:
                continue
            
                
        return result


        
        