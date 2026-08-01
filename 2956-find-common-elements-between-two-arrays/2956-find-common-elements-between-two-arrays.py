class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
        for i in nums2:
            if i in nums1:
                b.append(i)
        return [len(a),len(b)]

            
        