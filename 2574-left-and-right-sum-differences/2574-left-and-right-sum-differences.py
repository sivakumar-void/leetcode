class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]
        rs=[0]
        result=[]
        x=len(nums)-1
        for i in range(len(nums)-1):
            a=ls[len(ls)-1]
            b=rs[len(rs)-1]
            ls.append(a+nums[i])
            rs.append(b+nums[x])
            x-=1
        rs=rs[::-1]
        for i in range(len(ls)):
            result.append(abs(ls[i]-rs[i]))
        return result

        

        