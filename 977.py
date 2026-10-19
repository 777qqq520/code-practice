from typing import List
# 法一：直接排序
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num*num for num in nums)

# 法二：双指针--通过找到界限，得到负数，非负数两个有序子数组，最后归并排序
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        negative = -1
        for i,num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break
        i,j = negative,negative + 1
        ans = list()
        while i >= 0 or j < n:
            if j == n:
                ans.append(nums[i]*nums[i])
                i -= 1
            elif i < 0:
                ans.append(nums[j]*nums[j])
                j += 1 
            elif nums[i]*nums[i]>nums[j]*nums[j]:
                ans.append(nums[j]*nums[j])
                j += 1
            else:
                ans.append(nums[i]*nums[i])
                i -= 1
        return ans


# 法三：双指针--精髓在于从两端向中间遍历，比较绝对值大小，较大的平方放在结果数组的末尾
class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n 
        i,j,pos = 0,n-1,n-1
        while i <= j:
            if nums[i]*nums[i]<nums[j]*nums[j]:
                ans[pos] = nums[j]*nums[j]
                j -= 1
            else:
                ans[pos] = nums[i]*nums[i]
                i += 1
            pos -= 1
        return ans
        