#法一：滑动窗口（只适合数组中全是正数）
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:   #如果数组是空，直接返回
            return 0
        n = len(nums)
        ans = n + 1
        start,end = 0,0
        total = 0
        while end < n:   #外层循环：end不断向右扩张窗口，走到数组末尾停止
            total += nums[end]
            while total >= target:    #内层循环：和大于target时，start向右收缩窗口
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n+1 else  ans


#法二：暴力破解
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:   #先判断数组是否为空
            return 0 
        n = len(nums)
        ans = n + 1
        for i in range(n):
           total = 0
           for j in range(i,n):
               total += nums[j]
               if total >= target:
                    ans = min(ans,j-i+1)
                    break
        return 0 if ans == n+1 else ans