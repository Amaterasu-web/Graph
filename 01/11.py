#созданние графа
class Graph:
    def __init__(self):
        self.vertices: List[int] = []
        self.edges: Dict[int, List[int]] = {}

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges[vertex1].append(vertex2)
            self.edges[vertex2].append(vertex1)

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")
graph.add_edge("E", "F")
graph.add_edge("F", "G")
graph.add_edge("G", "F")
print(graph.edges)

#поиск в ширину

from collections import deque
from typing import List, Dict

def bfs(graph: Dict[int, List[int]], start_vertex: int) -> List[int]:
    visited = []
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]) - set(visited))

    return visited

graph_1 = {"A": ["B", "C", "D"], "B": ["C"], "C": ["D", "E"], "D": ["E"], "E": ["F"], "F": ["G"], "G": ["F"]}
print(bfs(graph_1, "A"))

#поиск в глубину
def dfs(graph: Dict[int, List[int]], start_vertex: int) -> List[int]:
    visited = []
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))

    return visited
graph_2 = {"A": ["B", "C", "D"], "B": ["C"], "C": ["D", "E"], "D": ["E"], "E": ["F"], "F": ["G"], "G": ["F"]}
print(dfs(graph_2, "A"))