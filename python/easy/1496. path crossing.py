class Solution:
    def isPathCrossing(self, path: str) -> bool:
        c, d = 0, 0
    
        visited = {(0, 0)}
        
        for i in path:
            if i == "N":
                c += 1
            elif i == "E":
                d += 1
            elif i == "S":
                c -= 1
            else:
                d -= 1
            
           
            if (c, d) in visited:
                return True
                
   
            visited.add((c, d))
            
        return False
