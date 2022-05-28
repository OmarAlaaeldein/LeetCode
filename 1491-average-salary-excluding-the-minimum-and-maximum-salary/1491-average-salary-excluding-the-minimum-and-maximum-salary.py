class Solution:
    def average(self, salary: List[int]) -> float:
        maxx=max(salary)
        minn=min(salary)
        summ=sum(salary)
        summ=summ-minn-maxx
        return summ/(len(salary)-2)
                