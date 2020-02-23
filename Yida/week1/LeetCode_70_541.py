class Solution(object):

    #  ±º‰∏¥‘”∂»£∫O(n)
    def climbStairs(self, n):
        if n <= 2: return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
