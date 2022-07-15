class Dijkstra(object):
    def __init__(self,graph,start_vertex):
        self.grid = graph
        self.length = len(graph)
        self.result = [float('inf') for _ in range(len(graph))]
        self.start_vertex = start_vertex
        self.result[start_vertex] = 0
        self.not_found = [graph[start_vertex][i] for i in range(len(graph))]
        self.not_found[self.start_vertex] = -1
        self.dic = {i:chr(ord('A')+i) for i in range(len(self.grid))}
        self.path = []
    def run(self):
        curr_vertex = self.start_vertex
        self.path.append(self.dic[curr_vertex])
        print('result: ',self.result)
        print('not found: ',self.not_found)
        for _ in range(1,self.length):
            print('当前节点为: ',curr_vertex)
            # find the vertex with the shortest distance

            next_vertex = None
            distance_between_curr_and_next = float('inf')
            for j in range(self.length):
                if 0 < self.not_found[j] < distance_between_curr_and_next:
                    next_vertex = j
                    distance_between_curr_and_next = self.not_found[j]
            print(f'下一个节点为: ',next_vertex)
            print(f'当前节点到下一个节点的距离为{distance_between_curr_and_next}')
            # Remove the shortest vertex and place it in the result
            self.result[next_vertex] = self.not_found[next_vertex]
            self.not_found[next_vertex] = -1
            # refresh the not_found list
            # 2.1 Iterate over the exit of the shortest point just found
            for rest_vertex in range(self.length):
                # Current vertex is passable and next vertex is not in the list of self.result
                if 0< self.grid[next_vertex][rest_vertex] and self.not_found[rest_vertex] != -1:
                    self.not_found[rest_vertex] = self.result[next_vertex]+self.grid[next_vertex][rest_vertex]
            curr_vertex = next_vertex
            self.path.append(self.dic[curr_vertex])
            print('result: ',self.result)
            print('not found: ',self.not_found)
        print('path: ',self.path)
        return self.result,self.path
if __name__ == '__main__':
    graph = [
        [ 0, 2, float('inf'), 6],
        [ 2, 0,  3, 2],
        [float('inf'), 3,  0, 2],
        [ 6, 2,  2, 0],
    ]

    dijkstra = Dijkstra(graph,0)
    print(dijkstra.run()) 