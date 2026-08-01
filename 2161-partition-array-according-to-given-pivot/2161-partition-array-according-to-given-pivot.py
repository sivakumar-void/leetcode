class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre=[]
        mid=[]
        post=[]
        for i in nums:
            if i<pivot:
                pre.append(i)
            elif i>pivot:
                post.append(i)
            else:
                mid.append(i)
        return pre+mid+post
            
        