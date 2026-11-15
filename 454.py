from ast import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        for a in nums1:
            for b in nums2:
                current_num = a + b
                if current_num in sum_map:
                    sum_map[current_num] += 1
                else:
                    sum_map[current_num] = 1
        count = 0
        for c in nums3:
            for d in nums4:
                target_num = c + d
                if -target_num in sum_map:
                    count += sum_map[-target_num]
        return count