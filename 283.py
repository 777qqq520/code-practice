#法一：将b后全填0,两轮
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[b] = nums[i]
                b += 1
        while b < len(nums):
            nums[b] = 0
            b += 1

#法二：交换
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        b = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[b] = nums[b], nums[i]
                b += 1