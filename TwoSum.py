class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        return []