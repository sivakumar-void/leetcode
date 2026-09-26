class Solution:
    def frequencySort(self, s: str) -> str:
        a=set(s)
        hs={}
        for i in a:
            hs[i]=s.count(i)
        hs=dict(sorted(hs.items(),key=lambda x:x[1],reverse=True))
        result=""
        for i in hs:
            result+=i*hs[i]
        return result
        
        
        
        


        