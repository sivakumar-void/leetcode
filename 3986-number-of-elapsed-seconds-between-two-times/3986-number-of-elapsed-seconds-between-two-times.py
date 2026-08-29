class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1,h2=int(startTime[:2])*60*60,int(endTime[:2])*60*60
        m1,m2=int(startTime[3:5])*60,int(endTime[3:5])*60
        s1,s2=int(startTime[6:8])+h1+m1,int(endTime[6:8])+h2+m2
        return s2-s1


        