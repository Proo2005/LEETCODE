class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empties = numBottles
        
        while empties >= numExchange:
            newBottles = empties // numExchange
            drank += newBottles
            empties = (empties % numExchange) + newBottles
            
        return drank
