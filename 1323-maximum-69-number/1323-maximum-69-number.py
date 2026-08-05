class Solution:
    def maximum69Number (self, num: int) -> int:
        combs=[]

        for i in range(len(str(num))):
            b=list(str(num))
            if b[i]=="6":
                
                b[i]="9"
            combs.append(int("".join(b)))
        return max(combs)
