class Solution:
    def average(self, salary: List[int]) -> float:
        minn=1000000
        maxx=0
        minni=0
        maxxi=0
        for i in range(len(salary)):
            if salary[i]>maxx:
                maxx=salary[i]
                maxxi=i
            if salary[i]<minn:
                minn=salary[i]
                minni=i
        if minni < maxxi:
            salary.pop(minni)
            salary.pop(maxxi-1)
        else:
            salary.pop(maxxi)
            salary.pop(minni-1)
        return sum(salary)/len(salary)
                