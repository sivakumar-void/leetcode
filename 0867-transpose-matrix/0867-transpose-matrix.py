class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix)==1:
            return [[matrix[0][i]] for i in range(len(matrix[0]))]
        else:
            result=[]
            for i in range(len(matrix[0])):
                temp=[]
                for j in range(len(matrix)):
                    temp.append(matrix[j][i])
                result.append(temp)
            return result

        