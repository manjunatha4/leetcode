class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        g=0
        index=0
        if sum(gas)< sum(cost):
            return -1
        for i in range(len(gas)):
            g=g+gas[i]-cost[i]
            if g<0:
                index=i+1
                g=0
        return index