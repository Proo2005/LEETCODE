class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start:destination])

        total = sum(distance)
        counter_clockwise = total - clockwise

     
        return min(clockwise, counter_clockwise)
