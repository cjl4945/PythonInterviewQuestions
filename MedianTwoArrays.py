import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst = sorted(lst)
        if len(lst) % 2 == 0:
            first = lst[math.ceil(len(lst) // 2) - 1]
            second = lst[math.floor(len(lst)//2)]

            median = (first + second) / 2
            return median
        median = lst[(len(lst) - 1)//2]
        return median


nums1 = [1, 2]
nums2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
