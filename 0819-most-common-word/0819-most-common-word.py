class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.lower()

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        para = paragraph.split()
        words = set(para)

        word = ""
        count = 0

        for i in words:
            if i in banned:
                continue

            a = para.count(i)

            if a > count:
                word = i
                count = a

        return word
        
        