class Solution:

    # first trial
    def maxArea1(self, height) -> int:
        i, j = 0, len(height) - 1
        max_vol = 0
        max_i, max_j = i, j
        while j > i:
            w = j - i
            h = min(height[i], height[j])
            vol = w * h
            if vol > max_vol:
                max_vol = vol
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_vol

    # second trial ->  just to write shorter code
    def maxArea2(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            l, r = (l + 1, r) if height[l] < height[r] else (l, r - 1)
        return res