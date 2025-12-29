
from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        mp = defaultdict(list)
        for pat in allowed:
            mp[pat[:2]].append(pat[2])

        def dfs(row):
            if len(row) == 1:
                return True

          
            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs("".join(path))

                pair = row[i:i+2]
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    path.append(ch)
                    if build_next(i + 1, path):
                        return True
                    path.pop()

                return False

            return build_next(0, [])

        return dfs(bottom)
