class Solution:
    # 从i出发到x前便停下，则任何[i,x-1]之间出发均不行
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0
        return start