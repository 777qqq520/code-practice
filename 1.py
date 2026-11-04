#法一：暴力破解
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        raise ValueError("Not two sum solution")


#法二：哈希表
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            complement = target - nums[i]
            if complement in hashmap:
                return[hashmap[complement],i]
            hashmap[num] = i
        raise ValueError("no two sum to solution")