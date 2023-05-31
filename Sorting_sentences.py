class Solution:
    def sortSentence(self, s: str) -> str:
        d=[]
        for i in s.split():
            d.append([i[-1], i[:-1]])
        d.sort()
        b=[]
        for i in d:
            b.append(i[1])
        return (' '.join(b))