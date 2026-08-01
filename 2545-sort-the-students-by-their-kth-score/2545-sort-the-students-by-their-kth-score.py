class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        srt=[score[i][k] for i in range(len(score))]
        a=sorted(srt)[::-1]
        result=[]
        for i in range(len(srt)):
            result.append(score[srt.index(a[i])])
        return result


        

        