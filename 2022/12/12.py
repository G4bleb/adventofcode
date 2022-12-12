from typing import TypeVar
import math

# Used for type hinting within class
DijkstraNodeType = TypeVar("DijkstraNodeType", bound="DijkstraNode")


class DijkstraNode:
    def __init__(self, val_str: str) -> None:
        self.visited = False
        self.val = ord(val_str)
        self.neighbours: list[tuple(DijkstraNode, int)] = []
        self.tentative_distance = math.inf

    def add_potential_neighbour(self, potential_neighbour: DijkstraNodeType) -> None:
        if potential_neighbour.val - self.val <= 1:
            self.neighbours.append((potential_neighbour, 1))

    def build_neighbours(self, x: int, y: int, mat: list[list[DijkstraNodeType]]) -> None:
        if x > 0:
            self.add_potential_neighbour(mat[y][x-1])
        if x < len(mat[0]) - 1:
            self.add_potential_neighbour(mat[y][x+1])
        if y > 0:
            self.add_potential_neighbour(mat[y-1][x])
        if y < len(mat) - 1:
            self.add_potential_neighbour(mat[y+1][x])


def solve1():
    with open('input.txt', 'r') as f:
        lines = [list(l.rstrip()) for l in f.readlines()]

    # Create node matrix
    nodes: list[list[DijkstraNode]] = []
    for line in lines:
        nodes.append([])
        for char in line:
            if char == 'S':
                start = DijkstraNode('a')
                start.tentative_distance = 0
                nodes[-1].append(start)
            elif char == 'E':
                end = DijkstraNode('z')
                nodes[-1].append(end)
            else:
                nodes[-1].append(DijkstraNode(char))

    # Build neghbours of nodes
    unvisited_nodes: set[DijkstraNode] = set()
    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            nodes[y][x].build_neighbours(x, y, nodes)
            unvisited_nodes.add(nodes[y][x])

    # Dijkstra Pathfinding
    current = start
    while unvisited_nodes:
        for n in current.neighbours:
            distance = current.tentative_distance + n[1]
            n[0].tentative_distance = min(n[0].tentative_distance, distance)
        current.visited = True
        unvisited_nodes.remove(current)
        if end.visited:
            print(end.tentative_distance)
            return
        current = min(unvisited_nodes, key=lambda n: n.tentative_distance)


def solve2():
    with open('input.txt', 'r') as f:
        lines = [list(l.rstrip()) for l in f.readlines()]

    # Create node matrix
    nodes: list[list[DijkstraNode]] = []
    for line in lines:
        nodes.append([])
        for char in line:
            if char == 'S':
                start = DijkstraNode('a')
                start.tentative_distance = 0
                nodes[-1].append(start)
            elif char == 'E':
                end = DijkstraNode('z')
                nodes[-1].append(end)
            else:
                node = DijkstraNode(char)
                if char == 'a':
                    node.tentative_distance = 0
                nodes[-1].append(node)

    # Build neghbours of nodes
    unvisited_nodes: set[DijkstraNode] = set()
    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            nodes[y][x].build_neighbours(x, y, nodes)
            unvisited_nodes.add(nodes[y][x])

    # Dijkstra Pathfinding
    current = start
    while unvisited_nodes:
        for n in current.neighbours:
            distance = current.tentative_distance + n[1]
            n[0].tentative_distance = min(n[0].tentative_distance, distance)
        current.visited = True
        unvisited_nodes.remove(current)
        if end.visited:
            print(end.tentative_distance)
            return
        current = min(unvisited_nodes, key=lambda n: n.tentative_distance)


solve1()
solve2()
