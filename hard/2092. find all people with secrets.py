from collections import defaultdict
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        meetings.sort(key=lambda x: x[2])
        
        know = set([0, firstPerson])
        i = 0

        while i < len(meetings):
            time = meetings[i][2]
            parent = {}

            def find(x):
                parent.setdefault(x, x)
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[py] = px

            people = set()

            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                people.add(x)
                people.add(y)
                i += 1

            groups = {}
            for p in people:
                root = find(p)
                groups.setdefault(root, []).append(p)

            for group in groups.values():
                if any(p in know for p in group):
                    know.update(group)

        return list(know)
