# Iterative Solution
class Solution:
    l=[]
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low,high=0,len(s)-1
        while low<high:
            s[low],s[high]=s[high],s[low]
            low+=1
            high-=1
""" 
# Recursive Solution
class Solution:
    l=[]
    def reverseString(self, s: List[str]) -> None:
        low,high=0,len(s)-1
        def help(s,low,high):
            if low<high:
                s[low],s[high]=s[high],s[low]
                help(s,low+1,high-1)
            else:
                return
        help(s,low,high)
"""