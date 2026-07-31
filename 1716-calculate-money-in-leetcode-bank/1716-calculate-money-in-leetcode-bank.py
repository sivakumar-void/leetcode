class Solution:
    def totalMoney(self, n: int) -> int:
        
        
        if n<=7:
            return sum(i for i in range(1,n+1))
        else:
            start=1
            end=7
            m=n
            
            b=[]
            
            for i in range(n//7):
                b.extend([i for i in range(start,end+1)])
                start+=1
                end+=1
                m-=7
            b.extend([x for x in range(start,start+m)])
            return sum(b)
            
            
            

              