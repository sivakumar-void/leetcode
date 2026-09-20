class Solution:
    def dayOfYear(self, date: str) -> int:
        mm=int(date[5:7])
        dd=int(date[8:10])
        year=int(date[0:4])
        a=[31,29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,31,30,31,30,31,31,30,31,30,31]
        return sum(a[:mm-1])+dd
        
        