from typing import List


class Solution:
    def moveZerosSolution1(self, nums: List[int]) ->None:
        """
        ����һ: ����һ���������飬ʣ�µ�������� ʱ�临�Ӷ�: O(n)���ռ临�Ӷ�O(n), ����ԭ�أ�in-place���ⷨ
        :param nums:
        :return:
        """
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * count

    def moveZerosSolution2(self, nums: List[int]) ->None:
        """
        ������: ��0�����ڱ��ڵ㣬�ѷ�0Ԫ����0Ԫ�ؽ���λ�ã������Ļ����Ա�֤ԭ����Ԫ�ص�λ�� ʱ�临�Ӷ�: O(n) �ռ临�Ӷ�O(1) ԭ�ؽⷨ
        :param nums:
        :return:
        """
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
