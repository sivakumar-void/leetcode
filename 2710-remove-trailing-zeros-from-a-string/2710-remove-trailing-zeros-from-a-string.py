class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        a=[i for i in str(num)]
        for i in range(len(a)):
            if a[len(a)-1]=="0":
                a.pop()
            else:
                break
        return "".join(a)

        

        