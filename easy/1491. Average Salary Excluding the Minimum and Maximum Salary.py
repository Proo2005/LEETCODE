class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary) - max(salary) - min(salary)
        count = len(salary) - 2
        return total / float(count)
