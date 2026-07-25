class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result=[0]
        b=0

        for i in range(len(gain)):
            b+=gain[i]
            result.append(b)
            
        return max(result)
        