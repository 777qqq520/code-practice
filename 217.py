#法一：
class Solution:
     def containsDuplicate(self, nums: list[int]) -> bool:
         x = set()
         for num in nums:
             if num in x:
                 return True
             else:
                 x.add(num)
         return False

#法二：
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))  