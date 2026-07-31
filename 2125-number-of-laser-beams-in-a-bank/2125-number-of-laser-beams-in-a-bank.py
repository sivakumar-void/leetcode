class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a=[x.count("1") for x in bank if x.count("1")!=0]
        if len(a)==1 or len(a)==0:
            return 0
        else:
            result=0
            for i in range(len(a)-1):
                result+=(a[i]*a[i+1])
            return result


        