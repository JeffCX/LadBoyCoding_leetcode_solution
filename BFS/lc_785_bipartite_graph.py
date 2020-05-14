from queue import Queue

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        """
            1. create the graph
            2. assign colors to each node
                if the next node is visited and have the same color, then it is not bipartite
            3. assign color level by level, return True
            
            Breath first search
            
            Time Complexity: O(v + n), v is the vertices, n is the nubmer of edges
        """
        
        # create the graph
        
        graph_dic = {}
        node_nums = len(graph)
        for node in range(node_nums):
            edges = graph[node]
            graph_dic[node] = edges
        
        # BFS, we define 0 as red, 1 as blue
        q = Queue()
        color_dic = {}
        
        def bfs(q, color_dic, node):
            
            q.put((node,0))
            while not q.empty():
                cur, color = q.get()
                if cur not in color_dic:
                    color_dic[cur] = 0
                for next_node in graph_dic[cur]:
                    if next_node not in color_dic:
                        new_color = color ^ 1
                        color_dic[next_node] = new_color
                        q.put((next_node, new_color))
                    else:
                        if color_dic[cur] == color_dic[next_node]:
                            return False
            return True
        
        for node in range(node_nums):
            if not bfs(q, color_dic, node):
                return False
        return True
            
        
                    
                
        
        
        
