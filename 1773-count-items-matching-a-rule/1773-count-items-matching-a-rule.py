class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result=0
        for i in range(len(items)):
            if ruleKey=="type":
                if items[i][0]==ruleValue:
                    result+=1
            elif ruleKey=="color":
                if items[i][1]==ruleValue:
                    result+=1
            else:
                if items[i][2]==ruleValue:
                    result+=1
        return result

        