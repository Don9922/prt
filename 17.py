from collections import deque
# Adjacency list for BFS
graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def bfs(graph, start):
    visited, queue, result = set(), deque([start]), []
    visited.add(start)
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor); queue.append(neighbor)
    return result
# Adjacency matrix for DFS
nodes = ['A','B','C','D','E','F']
matrix = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,1,0,0,0,0],
    [0,1,0,0,0,1],
    [0,0,1,0,1,0]
]
def dfs(matrix, nodes, start):
    visited, stack, result = set(), [start], []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node); result.append(node)
            idx = nodes.index(node)
            for i in range(len(nodes)-1, -1, -1):
                if matrix[idx][i] == 1 and nodes[i] not in visited:
                    stack.append(nodes[i])
    return result
print("BFS from A:", bfs(graph_list, 'A'))
print("DFS from A:", dfs(matrix, nodes, 'A'))