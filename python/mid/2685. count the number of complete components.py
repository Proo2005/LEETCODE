from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        a = {i: [] for i in range(n)}
        for u, v in edges:
            a[u].append(v)
            a[v].append(u)  

        visited = set()
        complete_components = 0

        for i in range(n):
            if i not in visited:
                component_node = []
                queue = deque([i])
                visited.add(i)

                while queue:
                    current = queue.popleft()
                    component_node.append(current)

                    for neighbour in a[current]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                            
           
                v_count = len(component_node)
                total_degree = sum(len(a[node]) for node in component_node)

                if total_degree == v_count * (v_count - 1):
                    complete_components += 1
                    
        return complete_components
