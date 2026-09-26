class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        
        r=[n,int(str(n)[::-1])]
        result=[]
        for i in range(min(r),max(r)+1):
            if i==1:
                continue
            if i==2:
                result.append(2)
                continue
            t=int(i**0.5)
            count=0
            for j in range(2,t+1):
                if i%j==0:
                    count+=1
            if count==0:
                result.append(i)
        return sum(result)


        