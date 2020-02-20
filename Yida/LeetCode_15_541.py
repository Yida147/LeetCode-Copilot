from typing import List


class Solution:
    def treeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        if not nums or n<3:
            return []
        for i in range(n):
            # 从小到大排序后第一位最小的数都大于0代表三数之和必定大于0
            if nums[i] > 0:
                return res
            # 遇到加过的pivot直接跳过
            if i > 0 and nums[i] == nums[i -1]:
                continue
            # 左右指针夹逼
            left = i +1
            right = n - 1
            while left < right:
                # 如果正好为零，记录结果
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    # 遇到加过的左指针或右指针直接跳过
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    # 完成循环
                    left += 1
                    right -= 1
                # 如果和大于零，说明三数之和偏大，由于排过序，移动右指针可以使三数之和变小
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                # 如果和大于零，说明三数之和偏小，由于排过序，移动左指针可以使三数之和变大
                else:
                    left += 1
        return res
