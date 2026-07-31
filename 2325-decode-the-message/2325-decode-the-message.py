class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a={}
        alpha="abcdefghijklmnopqrstuvwxyz"
        ind=0
        
        for i in key:
            if i != " " and i not in a:
                a[i]=alpha[ind]
                ind+=1
            

            
        result=""

        for i in message:
            if i in a:
                result+=a[i]
            else:
                result+=" "
            
        return result
        

        