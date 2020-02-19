class Solution:

    # basic idea, space complexity O(k), 但是实际提交出来的Runtime和memory并不差
    def rotate1(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) <= 1 or k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

    # Reverse，通过三次翻转数组得到结果，time complexity = O(n), space complexity = O(1)
    def rotate2(self, nums, k: int) -> None:

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

    # cyclic replacement，time complexity = O(n), space complexity = O(1)
    def rotate3(self, nums, k: int) -> None:

        k = k % len(nums)
        start = 0
        count = 0
        while count < len(nums):
            p = start
            last = nums[p - k]
            while True:
                nums[p], last = last, nums[p]
                p = (p + k) % len(nums)
                count += 1
                if p == start:
                    break
            start += 1

