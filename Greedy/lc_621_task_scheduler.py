from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # first: get the frequency of each task
        task_dic = {}
        for task in tasks:
            if task in task_dic:
                task_dic[task] += 1
            else:
                task_dic[task] = 1
                
        # put the task into a max heap
        heap = []
        
        for task in task_dic.keys():
            frequency = task_dic[task]
            if frequency > 0:
                heappush(heap, -frequency)
                
        # use max heap and a pending task array to model the CPU execuation
        time = 0
        
        while heap:
            
            pending_task = []
            i = 0
            while i <= n:
                if heap:
                    task = -heappop(heap)
                    if task > 1:
                        pending_task.append(task-1)
                time += 1
                
                if not heap and not pending_task:
                    break
                i += 1
            
            for task in pending_task:
                heappush(heap, -task)
        
        return time