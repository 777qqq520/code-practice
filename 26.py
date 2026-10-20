class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        b = 0
        for i in range(len(nums)):
            if nums[i] != nums [b]:   # b是慢指针(注意：如果相等，b也不用后移)
                b += 1     #遇到可放入的新数，先往后移
                nums[b] = nums[i]
        return b+1