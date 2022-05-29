from queue import Queue

class Node:
    def __init__(self, label, delay):
        self.label = label
        self.delay = delay

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        d = [-1]*(n+1)
        cost = [[-1 for i in range(n+1)] for j in range(n+1)]
        for t in times:
            cost[t[0]][t[1]] = t[2]
            
        q = Queue()
        q.put(Node(k, 0))
        d[k] = 0
        visited = {k: 1}
        while not q.empty():
            node = q.get()
            visited[node.label] = 1
            for i in range(len(cost[node.label])):
                if i != node.label and cost[node.label][i] >= 0:
                    delay = node.delay+cost[node.label][i]
                    if d[i] == -1:
                        d[i] = delay
                    elif d[i] > delay:
                        d[i] = delay
                    else:
                        continue                        
                    q.put(Node(i, delay))
                    
        if len(visited.keys()) < n:
            return -1
        
        mx = 0
        for i in range(len(d)):
            mx = max(mx, d[i])
        return mx
