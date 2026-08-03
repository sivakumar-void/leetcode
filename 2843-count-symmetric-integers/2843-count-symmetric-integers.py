class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            temp=[int(x) for x in str(i)]
            if len(temp)%2==1:
                continue
            lentemp=int(len(temp)/2)
            if sum(temp[:lentemp])==sum(temp[lentemp:]) :
                count+=1
        return count 
        