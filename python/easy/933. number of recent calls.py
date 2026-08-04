from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        min_time = t - 3000
        while self.queue and self.queue[0] < min_time:
            self.queue.popleft()
        return len(self.queue)
