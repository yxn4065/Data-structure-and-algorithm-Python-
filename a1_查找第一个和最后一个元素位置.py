# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/3/5 20:32 
# @IDE : PyCharm(2021.3.1) Python3.9.10
class Solution:
    # 寻找左边界
    def leftMargin(self, nums: list[int], target: int):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 如果 nums[mid] = target，继续向左寻找左边界
            if nums[mid] == target:
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[low] == target:
            return low
        # 如果左边界的值不等于 target
        else:
            return -1

    # 寻找右边界
    def rightMargin(self, nums: list[int], target: int):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 如果 nums[mid] = traget，继续向右寻找右边界
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[high] == target:
            return high
        # 如果右边界的值不等于 target
        else:
            return -1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # 首先判断 target 的范围
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        lm = self.leftMargin(nums, target)
        rm = self.rightMargin(nums, target)

        return [lm, rm]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    beau = Solution()
    print(beau.searchRange(nums, target))
