class Solution:
    def average(self, salary: List[int]) -> float:
        minn=1000000
        maxx=0
        summ=0
        for i in range(len(salary)):
            if salary[i]>maxx:
                maxx=salary[i]
            if salary[i]<minn:
                minn=salary[i]
            summ+=salary[i]
        summ=summ-minn-maxx
        return summ/(len(salary)-2)
                