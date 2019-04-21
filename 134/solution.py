class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        for i in range(len(gas)):
            if diff[i] >=0:
                gasamount = 0
                flag = True
                for j in range(len(gas)):
                    gasamount += diff[(i + j) % len(gas)]
                    if gasamount < 0:
                        flag = False
                        break
                if flag:
                    return i
        return -1
