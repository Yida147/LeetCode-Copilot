from typing import List


class Solution:
    def treeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        if not nums or n<3:
            return []
        for i in range(n):
            # ��С����������һλ��С����������0��������֮�ͱض�����0
            if nums[i] > 0:
                return res
            # �����ӹ���pivotֱ������
            if i > 0 and nums[i] == nums[i -1]:
                continue
            # ����ָ��б�
            left = i +1
            right = n - 1
            while left < right:
                # �������Ϊ�㣬��¼���
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    # �����ӹ�����ָ�����ָ��ֱ������
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    # ���ѭ��
                    left += 1
                    right -= 1
                # ����ʹ����㣬˵������֮��ƫ�������Ź����ƶ���ָ�����ʹ����֮�ͱ�С
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                # ����ʹ����㣬˵������֮��ƫС�������Ź����ƶ���ָ�����ʹ����֮�ͱ��
                else:
                    left += 1
        return res
