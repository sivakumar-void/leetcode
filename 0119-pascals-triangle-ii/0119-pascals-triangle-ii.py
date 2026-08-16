class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[[1],[1,1]]
        if rowIndex<2:
            return pascal[rowIndex]
        else:
            for i in range(rowIndex+1):
                temp=pascal[len(pascal)-1]
                temp2=[1,1]
                for j in range(len(temp)-1):
                    temp2.insert(1,temp[j]+temp[j+1])
                pascal.append(temp2)
            return pascal[rowIndex]
        

        