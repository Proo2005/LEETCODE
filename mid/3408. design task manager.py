import heapq

class TaskManager:
    def __init__(self, tasks):
        # taskId -> (priority, userId)
        self.task_map = {}
        # max-heap of (-priority, -taskId)
        self.heap = []
        
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (priority, userId)
            heapq.heappush(self.heap, (-priority, -taskId))
    
    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))
    
    def edit(self, taskId, newPriority):
        if taskId in self.task_map:
            userId = self.task_map[taskId][1]
            self.task_map[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId))
    
    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]
    
    def execTop(self):
        while self.heap:
            # Get the current top candidate
            neg_priority, neg_taskId = heapq.heappop(self.heap)
            taskId = -neg_taskId
            priority = -neg_priority
            # Check if it still exists and matches the current priority
            if taskId in self.task_map and self.task_map[taskId][0] == priority:
                userId = self.task_map[taskId][1]
                del self.task_map[taskId]
                return userId
        return -1
