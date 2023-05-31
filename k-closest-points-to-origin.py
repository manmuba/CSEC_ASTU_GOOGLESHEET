class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        f=[]
        for i in points:
            n=((i[0]**2) + (i[1]**2))/2
            f.append([n, i])
        f.sort()
        g=[]
        for i in f:
            g.append(i[1])
        return (g[:k])