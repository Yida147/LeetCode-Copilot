from typing import List


class Solution:
    def moveZerosSolution1(self, nums: List[int]) ->None:
        """
        方法一: 生成一个非零数组，剩下的用零填充 时间复杂度: O(n)，空间复杂度O(n), 不是原地（in-place）解法
        :param nums:
        :return:
        """
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * count

    def moveZerosSolution2(self, nums: List[int]) ->None:
        """
        方法二: 把0看作哨兵节点，把非0元素与0元素交换位置，这样的话可以保证原来零元素的位置 时间复杂度: O(n) 空间复杂度O(1) 原地解法
        :param nums:
        :return:
        """
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
