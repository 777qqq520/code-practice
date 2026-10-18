class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        b = 0
        for a in range(len(nums)):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
        return b
