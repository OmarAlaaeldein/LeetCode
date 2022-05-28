class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = dict()
        for i in range(len(nums)):
            if dic.get(nums[i], None) == None:
                dic[nums[i]] = True
            elif dic.get(nums[i], None) == True:
                return 'true'