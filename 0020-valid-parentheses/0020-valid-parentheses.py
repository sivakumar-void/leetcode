class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        p={"(":")","{":"}","[":"]"}
        for i in s:
            if i in p.keys():
                st.append(i)
            else:
                if len(st)==0:
                    return False
                else:
                    if p[st[-1]]==i:
                        st.pop()
                    else:
                        return False
        return True if len(st)==0 else False
        