from typing import List
#法一：
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res_set = set()
        for num in set1:
            if num in set2:
                res_set.add(num)
        return list(res_set)

#法二：
class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3       return list(set(nums1) & set(nums2))