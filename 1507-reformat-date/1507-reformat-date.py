class Solution:
    def reformatDate(self, date: str) -> str:
        mon=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        temp=date.split()
        dd=temp[0][:2] if temp[0][1]  not in "trsn" else "0"+ temp[0][:1]
        mm=str(mon.index(temp[1])+1) if len(str(mon.index(temp[1])+1))==2 else "0"+str(mon.index(temp[1])+1)
        yy=temp[2]
        return f"{yy}-{mm}-{dd}"
        